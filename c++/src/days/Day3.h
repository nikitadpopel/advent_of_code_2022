#include <vector>
#include <string>

class Day3
{
    public:
        Day3();
        int Part1(std::vector<std::string> rucksacks);
        int Part2(std::vector<std::string> rucksacks);
        bool Solve();
    private:
        std::vector<std::string> m_vecInput;
};