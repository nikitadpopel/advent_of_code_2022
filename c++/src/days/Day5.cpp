#include <iostream>
#include <string>
#include <algorithm>

#include "Day5.h"
#include "../helpers/Reader.h"

Day5::Day5()
{
	//m_vecInput = ReadInput("../../../inputs/day5.txt");
	m_vecInput = ReadInput("../inputs/day5.txt");
	ParseInput();
	PrintCrates();
}

void Day5::ParseInput()
{

}

void Day5::PrintCrates()
{
	std::cout << "Crates:" <<std::endl;
}

int Day5::Part1(std::vector<std::string> moves)
{
    std::vector<std::string>::iterator iter;
	for(iter = moves.begin(); iter < moves.end(); iter++ )
	{   
		std::cout << *iter << std::endl;
	}
	return 0;
}

int Day5::Part2 (std::vector<std::string> moves)
{
    std::vector<std::string>::iterator iter;
	for(iter = moves.begin(); iter < moves.end(); iter++ )
	{   
		std::cout << *iter << std::endl;
	}
	return 0;
}

bool Day5::Solve()
{

	std::cout << Part1(m_vecInput) <<std::endl;
	std::cout << Part2(m_vecInput) <<std::endl;
	return true;
}