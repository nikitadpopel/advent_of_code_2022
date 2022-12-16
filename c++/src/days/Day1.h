#include <vector>
#include <string>

class Day1
{
    public:
        Day1();
        int Part1(std::vector<int>);
        int Part2(std::vector<int>);
        bool Solve();
    private:
        std::vector<std::string> m_vecInput;
};