#include <vector>
#include <string>

class Day5
{
    public:
        Day5();
        int Part1(std::vector<std::string> moves);
        int Part2(std::vector<std::string> moves);
        bool Solve();
    private:
        std::vector<std::string> m_vecInput;
};