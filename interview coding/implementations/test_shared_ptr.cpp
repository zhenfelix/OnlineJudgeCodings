#include<bits/stdc++.h>
#include "./shared_ptr.h"


struct Foo {
  Foo() { std::cout << "Foo created\n"; }
  ~Foo() { std::cout << "Foo destroyed\n"; }
  friend std::ostream& operator << (std::ostream& out, Foo& f);
  
};

std::ostream& operator << (std::ostream& out, Foo& f) {
    out << "foo";
    return out;
  }

struct Base {
  virtual void bar() { std::cout << "Base\n"; }
};

struct Derived: public Base {
  void bar() override { std::cout << "Derived\n"; }
};

int main() {
  // Test 1: Construct shared_ptr and verify the object is created
  {
    shared_ptr<Foo> p1(new Foo); // Foo created 
    std::cout << "Use count: " << p1.use_count() << '\n'; // outputs 1
    // std::cout << *p1 << '\n';
  } // Foo destroyed

  // Test 2: Copy construct shared_ptr and verify use count is updated
  {
    shared_ptr<Foo> p1(new Foo); // Foo created
    shared_ptr<Foo> p2(p1); 
    std::cout << "Use count: " << p1.use_count() << '\n'; // outputs 2
  } // Foo destroyed

  // Test 3: Copy assignment shared_ptr and verify use count is updated
  {
    shared_ptr<Foo> p1(new Foo); // Foo created 
    shared_ptr<Foo> p2(new Foo); // Foo created
    p1 = p2;  // Foo destroyed
    std::cout << "Use count: " << p1.use_count() << '\n'; // outputs 2
    std::cout << "Use count: " << p2.use_count() << '\n'; // outputs 2
  } // Foo destroyed

//   // Test 4: Reset shared_ptr and verify the original object is destroyed
//   {
//     shared_ptr<Foo> p1(new Foo); // Foo created 
//     p1.reset(nullptr); // Foo destroyed 
//   } 

//   // Test 5: Move shared_ptr and verify the moved-from instance has a nullptr
//   {
//     shared_ptr<Foo> p1(new Foo); // Foo created 
//     shared_ptr<Foo> p2 = std::move(p1);
//     std::cout << "Use count: " << p2.use_count() << '\n'; // outputs 1
//     std::cout << "p1 is null: " << (p1 ? "false" : "true") << '\n'; // outputs true
//   } // Foo destroyed 

//   // Test 6: Move assignment and verify the moved-from instance has a nullptr
//   {
//     shared_ptr<Foo> p1(new Foo); // Foo created 
//     shared_ptr<Foo> p2;
//     p2 = std::move(p1);
//     std::cout << "Use count: " << p2.use_count() << '\n'; // outputs 1
//     std::cout << "p1 is null: " << (p1 ? "false" : "true") << '\n'; // outputs true
//   } // Foo destroyed 

//   // Test 7: Generalized copy constructor with related types 
//   {
//     shared_ptr<Foo> p1(new Foo);  // Foo created 
//     shared_ptr<Foo> p2(p1); 
//     shared_ptr<const Foo> p3(p2);
//     std::cout << "Use count: " << p3.use_count() << '\n'; // outputs 3
//   } // Foo destroyed 


//   // Test 8: Generalized copy constructor with related types
//   {
//     shared_ptr<Derived> p1(new Derived); 
//     shared_ptr<Base> p2(p1);
//     p2->bar(); // outputs Derived
//   }

  return 0;
}