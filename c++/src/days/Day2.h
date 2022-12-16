#include <vector>
#include <string>

class Day2
{
    public:
        Day2();
        int Part1(std::vector<std::string> hands);
        int Part2(std::vector<std::string> hands);
        bool Solve();
    private:
        std::vector<std::string> m_vecInput;
};