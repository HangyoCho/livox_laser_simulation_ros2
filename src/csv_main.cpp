#include "csv_reader.hpp"

int main(int argc, char const* argv[]) {
    std::vector<std::vector<double>> datas;
    CsvReader::ReadCsvFile("/sros/avia.csv", datas);
    return 0;
}