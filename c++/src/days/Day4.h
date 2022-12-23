#include <vector>
#include <string>

class Day4
{
    public:
        Day4();
        int Part1(std::vector<std::string> sectionlist);
        int Part2(std::vector<std::string> sectionlist);
        bool Solve();
    private:
        std::vector<std::string> m_vecInput;
};