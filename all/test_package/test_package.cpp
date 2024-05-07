#include "confu_algorithm/createChainViews.hxx"
#include <iostream>

int
main ()
{
  std::cout << "create chains where all numbers are the same from: [ ";
  auto nums = std::vector{ 1, 1, 1, 2, 2, 3, 3, 3 };
  for (auto num : nums)
  {
    std::cout << num << ' ';
  }
  std::cout << ']' << std::endl;
  auto result = confu_algorithm::createChainViews (nums.cbegin (), nums.cend (), [] (auto begin,auto end) {
    auto const &lastItem = *(end - 1);
    auto const &secondLastItem = *(end - 2);
  return lastItem == secondLastItem;
  });
  for (auto sequence : result)
  {
    for (auto num : sequence)
    {
      std::cout << num << " ";
    }
    std::cout << std::endl;
  }
}
