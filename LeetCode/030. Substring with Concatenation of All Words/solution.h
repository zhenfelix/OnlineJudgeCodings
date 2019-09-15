class Solution {
private:
  class AcAutomaton {
  private:
    struct Node {
      Node* child[26]{};
      Node* fail{};
      // no next needed since all words have same length
      // Node* next{};
      size_t id{};
    };
  public:
    inline AcAutomaton(size_t nNode) :
      nodes(new Node[nNode]), queue(new Node*[nNode]) {}

    inline void add(string_view sv, vector<int>& ctr) {
      auto cur = &root;
      for (auto ch : sv) {
        auto key = (size_t) (ch - 'a');
        if (!cur->child[key])
          cur->child[key] = &nodes[nNode++];
        cur = cur->child[key];
      }
      if (cur->id)
        ++ctr[cur->id - 1];
      else {
        ctr.emplace_back(1);
        cur->id = ctr.size();
      }
    }

    inline void build() {
      root.fail = &root;
      size_t qEnd = 0;
      for (auto key = 0; key < 26; ++key)
        if (root.child[key]) {
          auto cur = root.child[key];
          cur->fail = &root;
          queue[qEnd++] = cur;
        }
      for (size_t qBeg = 0; qBeg != qEnd; ++qBeg)
        for (auto key = 0; key < 26; ++key)
          if (queue[qBeg]->child[key]) {
            auto cur = queue[qBeg]->child[key];
            auto fail = queue[qBeg]->fail;
            while (fail != &root && !fail->child[key])
              fail = fail->fail;
            cur->fail = fail->child[key] ? fail->child[key] : &root;
            queue[qEnd++] = cur;
          }
    }

    inline void match(vector<size_t>& ids, string_view sv, size_t lenWord) {
      auto fail = &root;
      for (size_t i = 0; i != sv.size(); ++i) {
        auto key = sv[i] - 'a';
        while (fail != &root && !fail->child[key])
          fail = fail->fail;
        if (fail->child[key]) {
          fail = fail->child[key];
          if (fail->id)
            ids[i - lenWord + 1] = fail->id;
        }
      }
    }

  private:
    unique_ptr<Node[]> nodes;
    unique_ptr<Node*[]> queue;
    Node root{};
    size_t nNode{};
  };
public:
  vector<int> findSubstring(string text, vector<string>& words) {
    if (text.empty() || words.empty() || words[0].empty())
      return {};
    auto lenText = text.size();
    auto nWord = words.size();
    auto lenWord = words[0].size();
    auto lenPattern = nWord * lenWord;
    if (lenText < lenPattern)
      return {};
    vector<size_t> ids(text.size());
    vector<int> ctrDict;
    ctrDict.reserve(nWord);
    {
      AcAutomaton aca(nWord * lenWord);
      for (auto& word : words)
        aca.add(word, ctrDict);
      aca.build();
      aca.match(ids, text, lenWord);
    }
    auto nDistWord = ctrDict.size();
    vector<int> ctrText(nDistWord);
    vector<int> res;
    for (size_t i = 0; i < lenWord && i + lenPattern <= lenText; ++i) {
      fill(ctrText.begin(), ctrText.end(), 0);
      auto nMatchedDistWord = 0;
      for (size_t j = i; j < i + lenPattern; j += lenWord) {
        if (ids[j]) {
          auto idx = ids[j] - 1;
          if (ctrText[idx]++ == ctrDict[idx])
            --nMatchedDistWord;
          if (ctrText[idx] == ctrDict[idx])
            ++nMatchedDistWord;
        }
      }
      if (nMatchedDistWord == nDistWord)
        res.emplace_back(i);
      for (size_t j = i + lenPattern; j < lenText; j += lenWord) {
        if (ids[j]) {
          auto idx = ids[j] - 1;
          if (ctrText[idx]++ == ctrDict[idx])
            --nMatchedDistWord;
          if (ctrText[idx] == ctrDict[idx])
            ++nMatchedDistWord;
        }
        if (ids[j - lenPattern]) {
          auto idx = ids[j - lenPattern] - 1;
          if (ctrText[idx]-- == ctrDict[idx])
            --nMatchedDistWord;
          if (ctrText[idx] == ctrDict[idx])
            ++nMatchedDistWord;
        }
        if (nMatchedDistWord == nDistWord)
          res.emplace_back(j - lenPattern + lenWord);
      }
    }
    return res;
  }
};