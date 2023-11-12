#ifndef GNN_PORT_SMART_PTR_HPP_INCLUDED
#define GNN_PORT_SMART_PTR_HPP_INCLUDED

/**
   An easy implementation of "smart pointer"

   The idea is just like shared_ptr in Boost C++ Library: it has a reference
   counter indicating when to delete the raw pointer.

   This file is a part of gnn C++ Library by L.INA.
*/

#include <algorithm> // swap

namespace gnn {
namespace port {
namespace sp {

/**
   Base class for deallocators.
   Deallocators must provide dispose and destroy method as its member
   and get method as its static member.
*/
struct deallocator_base {
    // base class for various deallocators
    virtual void dispose(void)=0; // deallocate containing object
    virtual void destroy(void)=0; // destroy deallocator itself if necessary
    virtual ~deallocator_base(void){}
};

namespace detail {

/**
   Deallocator for new / delete.
*/
template <class T>
struct simple_deallocator : public deallocator_base {
    typedef simple_deallocator<T> this_type;
    virtual void dispose(void){ delete p_; }
    virtual void destroy(void){ delete this; } // it knows itself how to die
    static this_type* get(T* p){ return new this_type(p); } // factory pattern
private:
    this_type& operator=(const this_type&){ return *this; }
protected:
    simple_deallocator(const this_type& rhs):p_(rhs.p_){} //forbidden
    simple_deallocator(void):p_(0){} // forbidden
    simple_deallocator(T* p):p_(p){} // forbidden from outisde
    T* p_;
};

/**
   Deallocator for new[] / delete[].
*/
template <class T>
struct array_deallocator : public deallocator_base {
    typedef array_deallocator<T> this_type;
    virtual void dispose(void){ delete[] p_; }
    virtual void destroy(void){ delete this; } // it knows itself how to die
    static this_type* get(T* p){ return new this_type(p); } // factory pattern
private:
    this_type& operator=(const this_type&){ return *this; }
protected:
    array_deallocator(const this_type& rhs):p_(rhs.p_){} // forbidden
    array_deallocator(void):p_(0){} // forbidden
    array_deallocator(T* p):p_(p){} // forbidden from outside
    T* p_;
};

} // namespace detail

/**
   Type information for generating a deallocator object of appropriate type.
   This hack looks ugly but is necessary since typedef templates are prohibited
   in C++ standard.
*/
struct simple_dealloc {
    template<class T> struct type : public detail::simple_deallocator<T> {
        typedef detail::simple_deallocator<T> name;
    };
};
struct array_dealloc {
    template<class T> struct type : public detail::array_deallocator<T> {
        typedef detail::array_deallocator<T> name;
    };
};

/**
   Reference counter.
*/
struct counted_ref {
    typedef counted_ref this_type;
    counted_ref(void):pn_(0){}
    counted_ref(const this_type& r):pn_(r.pn_){ if (pn_) pn_->inc(); }
    template<class S, class D>
    explicit counted_ref(S* p, D d):pn_(new impl(p,d)){}
    ~counted_ref(void){ release(); }
    void release(void) {
        if (pn_ && !pn_->dec()) {
            pn_->d_->dispose();
            delete pn_;
        }
    }
    void swap(counted_ref& r){ std::swap(pn_, r.pn_); }
    this_type& operator=(const this_type& r) {
        impl* tmp = r.pn_;
        if (tmp != pn_) {
            if (tmp) tmp->inc();
            release();
            pn_ = tmp;
        }
        return *this;
    }
    bool unique(void)const{ return use_count() == 1; }
    size_t use_count(void)const{ return pn_ ? pn_->count() : 0; }
private:
    struct impl {
        template<class S, class D> explicit impl(S* p, D)
            :n_(1),d_(D::template type<S>::name::get(p)){}
        impl(const impl& c):n_(c.n_),d_(c.d_){}
        size_t inc(void){ return ++n_; }
        size_t dec(void){ return --n_; }
        size_t count(void)const{ return n_; }
        ~impl(void){ d_->destroy(); } // d_ must exist or it is a fatal error
        size_t n_;
        deallocator_base* d_;
    private:
        impl& operator=(const impl&){ return *this; }
    };
    impl*  pn_;
};

/**
   Smart pointer.
   It provides managed pointer class with reference counter by default.
   Behavior can be changed by specifying RefObject template parameter.

   Costs of smart_ptr are:
   - a data size of each smart_ptr instance which consists of:
     * a data size of the pointer to the object
     * and a data size of the reference counter, that is a size of a pointer
       to the internal reference counter object,
   - a data size of the internal reference counter object, which is the one and
     only for the referred object managaed by smart_ptr
   - and a checking if the counter is zero or not acting each time the
     smart_ptr instance is destroyed or overridden by assignment.
*/
template<class T, class RefObject=counted_ref> struct smart_ptr {
    // type definitions
    typedef smart_ptr<T, RefObject> this_type;
    typedef RefObject refobj_type;
    typedef T         value_type;
    typedef T         element_type;
    typedef T*        pointer;
    typedef const T*  const_pointer;
    typedef T&        reference;
    typedef const T&  const_reference;

    // default constructor
    smart_ptr(void):px_(0),r_(){}
    // copy constructors
    smart_ptr(const this_type& s):px_(s.px_),r_(s.r_){}
    template<class S>
    smart_ptr(const smart_ptr<S, refobj_type>& s):px_(s.px_),r_(s.r_){}
    // constructors from a raw pointer
    template<class S>
    explicit smart_ptr(S* p):px_(p),r_(p,simple_dealloc()){}
    template<class S, class D>
    explicit smart_ptr(S* p, D d):px_(p),r_(p,d){}

    // destructor
    ~smart_ptr(void){}

    // primitive operations
    void reset(void){ this_type().swap(*this); }
    void reset(const this_type& s){ this_type(s).swap(*this); }
    template<class S> void reset(S* p){ this_type(p).swap(*this); }
    template<class S, class D>
    void reset(S* p, D d){ this_type(p, d).swap(*this); }
    void swap(this_type& other) {
        std::swap(px_, other.px_);
        r_.swap(other.r_);
    }

    // assignment
    this_type& operator=(const this_type& s) {
        px_ = s.px_;
        r_ = s.r_;
        return *this;
    }
    template<class S>
    this_type& operator=(const smart_ptr<S, refobj_type>& s) {
        px_ = s.px_;
        r_ = s.r_;
        return *this;
    }

    // references
    reference operator*()const{ return *get(); }
    pointer operator->()const{ return get(); }
    pointer get(void)const{ return px_; }

    // referece counter
    bool unique(void)const{ return r_.unique(); }
    size_t use_count(void)const{ return r_.use_count(); }

    // operators
    operator bool(void)const{ return !!px_; }
    bool operator!(void)const{ return !px_; }
private:
    template<class S, class R> friend struct smart_ptr;
    pointer px_;
    refobj_type r_;
};

// comparison to make a smart_ptr like a normal pointer
template<class T, class U, class R>
inline bool operator==(const smart_ptr<T,R>& lhs, const smart_ptr<U,R>& rhs) {
    return lhs.get() == rhs.get();
}
template<class T, class U, class R>
inline bool operator!=(const smart_ptr<T,R>& lhs, const smart_ptr<U,R>& rhs) {
    return lhs.get() != rhs.get();
}

}}}

#endif // !GNN_PORT_SMART_PTR_HPP_INCLUDED