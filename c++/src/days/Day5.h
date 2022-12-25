#include <vector>
#include <string>

class Day5
{
    public:
        Day5();
        void ParseInput();
        void PrintCrates();
        int Part1(std::vector<std::string> moves);
        int Part2(std::vector<std::string> moves);
        bool Solve();
    private:
        std::vector<std::string> m_vecInput;
        std::vector<std::string> m_moves;
        std::vector<std::vector<char>> m_crates;
};