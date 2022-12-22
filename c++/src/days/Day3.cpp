#include <iostream>
#include <string>
#include <algorithm>

#include "Day3.h"
#include "../helpers/Reader.h"

Day3::Day3()
{
	//m_vecInput = ReadInput("../../../inputs/day3.txt");
	m_vecInput = ReadInput("../inputs/day3.txt");
}

int Day3::Part1(std::vector<std::string> rucksacks)
{
    std::vector<std::string>::iterator iter;
	for(iter = rucksacks.begin(); iter < rucksacks.end(); iter++ )
	{   
        std::cout << *iter << std::endl;

	}
    return 0;
}

int Day3::Part2(std::vector<std::string> rucksacks)
{
    std::vector<std::string>::iterator iter;
	for(iter = rucksacks.begin(); iter < rucksacks.end(); iter++ )
	{   
        std::cout << *iter << std::endl;
	}
    return 0;
}

bool Day3::Solve()
{
	std::cout << Part1(m_vecInput) <<std::endl;
	std::cout << Part2(m_vecInput) <<std::endl;
	return true;
}