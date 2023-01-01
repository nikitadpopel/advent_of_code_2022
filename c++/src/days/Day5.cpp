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
	int index = 0;
	auto it = std::find(m_vecInput.begin(), m_vecInput.end(), "");
	if(it != m_vecInput.end())
	{
		index = it - m_vecInput.begin();
	}

	std::cout << "Index: " << index << std::endl;
	std::cout << "test: "<< m_vecInput[index - 1] << std::endl;
}

void Day5::PrintCrates()
{
	std::cout << "Crates:" <<std::endl;

	
	std::cout << "----------------------------------------------------" <<std::endl <<std::endl;
}

int Day5::Part1(std::vector<std::string> moves)
{
    // std::vector<std::string>::iterator iter;
	// for(iter = moves.begin(); iter < moves.end(); iter++ )
	// {   
	// 	std::cout << *iter << std::endl;
	// }
	return 0;
}

int Day5::Part2 (std::vector<std::string> moves)
{
    // std::vector<std::string>::iterator iter;
	// for(iter = moves.begin(); iter < moves.end(); iter++ )
	// {   
	// 	std::cout << *iter << std::endl;
	// }
	return 0;
}

bool Day5::Solve()
{

	std::cout << Part1(m_vecInput) <<std::endl;
	std::cout << Part2(m_vecInput) <<std::endl;
	return true;
}