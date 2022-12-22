#include <iostream>
#include <string>
#include <algorithm>

#include "Day1.h"
#include "../helpers/Reader.h"

Day1::Day1()
{
	//m_vecInput = ReadInput("../../../inputs/day1.txt");
	m_vecInput = ReadInput("../inputs/day1.txt");

}

int Day1::Part1(std::vector<int> elves)
{

	
	std::vector<int>::iterator iterelves;
	int max = 0;
	for(iterelves = elves.begin(); iterelves < elves.end(); iterelves++ )
	{
		if(*iterelves > max)
		{
			max = *iterelves;
		}
	}
	return max;
}

int Day1::Part2(std::vector<int> elves)
{
	std::sort(elves.begin(),elves.end(),std::greater<int>());
	return elves[0] + elves[1] + elves[2];
}

bool Day1::Solve()
{
	std::vector<int> elves;

	std::vector<std::string>::iterator iter;
	int currelf = 0;
	for(iter = m_vecInput.begin(); iter < m_vecInput.end(); iter++ )
	{
		if(!iter->empty())
		{
			currelf += stoi(*iter);
		}
		else
		{
			elves.push_back(currelf);
			currelf = 0;
		}
	}
	elves.push_back(currelf);

	std::cout << Part1(elves) <<std::endl;
	std::cout << Part2(elves) <<std::endl;

	return true;
}