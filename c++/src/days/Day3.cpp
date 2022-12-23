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
	int totalcount = 0;
	for(iter = rucksacks.begin(); iter < rucksacks.end(); iter++ )
	{   
		std::string rucksack = *iter;
		int rucksacksize = rucksack.length() / 2;
		std::vector<char> firsthalf;
		for(int i = 0; i < rucksacksize; i++)
		{
			firsthalf.push_back(rucksack[i]);
		}


		bool notfound = false;
		char value = ' ';
		for(int i = rucksacksize; i < rucksacksize * 2 && !notfound; i++)
		{
			auto result1 = std::find(firsthalf.begin(), firsthalf.end(), rucksack[i]);
			if(result1 != firsthalf.end())
			{
				value = *result1;
				notfound = true;
			}
		}

		int asciival = int(value);
		if(asciival > 96)
		{
			totalcount += asciival - 96;
		}
		else
		{
			totalcount += asciival - (64-26);
		}
	}
    
	return totalcount;
}

int Day3::Part2 (std::vector<std::string> rucksacks)
{
    std::vector<std::string>::iterator iter;
	int totalcount = 0;
	for(iter = rucksacks.begin(); iter < rucksacks.end(); iter+=3 )
	{   
		std::vector<char> secondstring;
		std::vector<char> thirdstring;
		
		std::string iteritem1 = *(iter);
		std::string iteritem2 = *(iter+1);
		std::string iteritem3 = *(iter+2);
		for(int i = 0; i < iteritem2.length(); i++)
		{
			secondstring.push_back(iteritem2[i]);
		}
		for(int i = 0; i < iteritem3.length(); i++)
		{
			thirdstring.push_back(iteritem3[i]);
		}

		bool notfound = false;
		char value = ' ';
		for(int i = 0; i < iteritem1.length() && !notfound; i++)
		{
			auto result2 = std::find(secondstring.begin(), secondstring.end(), iteritem1[i]);
			auto result3 = std::find(thirdstring.begin(), thirdstring.end(), iteritem1[i]);
			if(result2 != secondstring.end() && result3 != thirdstring.end())
			{
				value = iteritem1[i];
				notfound = true;
			}
		}
		
		int asciival = int(value);
		if(asciival > 96)
		{
			totalcount += asciival - 96;
		}
		else
		{
			totalcount += asciival - (64-26);
		}
	}
	
    return totalcount;
}

bool Day3::Solve()
{
	std::cout << Part1(m_vecInput) <<std::endl;
	std::cout << Part2(m_vecInput) <<std::endl;
	return true;
}