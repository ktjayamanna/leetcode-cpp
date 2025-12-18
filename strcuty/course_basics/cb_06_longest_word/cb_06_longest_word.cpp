// Longest Word
// Find the longest word in an array of words

/*
PROBLEM DESCRIPTION:
================================================================================
Write a function, longestWord, that takes in a sentence string as an argument. The function should return the longest word in the sentence. If there is a tie, return the word that occurs later in the sentence.

You can assume that the sentence is non-empty.


EXAMPLES:
================================================================================
longest_word(['cat', 'building', 'museum', 'a']) // -> 'building'
longest_word(['short', 'longer', 'longest']) // -> 'longest'
longest_word(['same', 'size']) // -> 'same'


CONSTRAINTS:
================================================================================
- Array will contain at least one word
- All elements are strings
- Return the first longest word if there are ties

*/

// SOLUTION:
// ================================================================================


#include <string>
#include <vector>
#include <iostream>
#include <cmath>

std::vector<std::string> split(const std::string& s, char delimiter){
  std::vector<std::string> tokens;
  size_t start = 0, end;
  while ((end = s.find(delimiter, start)) != std::string::npos){
    tokens.push_back(s.substr(start, end - start));
    start = end + 1;
  }
  tokens.push_back(s.substr(start));
  return tokens;
}

std::string longestWord(std::string sentence) {
  auto max_size = -INFINITY;
  std::string longest_word = "";
  auto words = split(sentence, ' ');
  for (auto& word : words){
    if (word.size() >= max_size){
      max_size = word.size();
      longest_word = word;
    }
  }
  return longest_word;
}

void run() {
  // this function behaves as `main()` for the 'run' command
  // you may sandbox in this function, but should not remove it

}