// uniform_int_distribution::operator()
#include <iostream>
#include <chrono>

#include <random>
#include <functional>

#include <iomanip>
#include <map>

int main()
{
	std::random_device rd{};
	std::mt19937 gen{rd()};

	std::normal_distribution<> d{5,2};
	auto gauss52 = std::bind(d, gen);

	std::map<int, int> hist{};
	for(int n=0; n<10000; ++n) {
	 ++hist[std::round(gauss52())];
	}
  			
  	for(auto p : hist) {
  	    std::cout << std::setw(2) << p.first << ' ' << std::string(p.second/200, '*') << '\n';
    }

  return 0;
}