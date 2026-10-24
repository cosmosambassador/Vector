// SPDX-License-Identifier: LGPL-2.1-only
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    if (argc > 3) {
        std::cerr << "Use: bew_packet [unix|apple|android|microsoft] [none|ibm|qwen]\n";
        return 2;
    }
    const std::string platform = argc > 1 ? argv[1] : "unix";
    const std::string provider = argc > 2 ? argv[2] : "none";
    if ((platform != "unix" && platform != "apple" && platform != "android" && platform != "microsoft") ||
        (provider != "none" && provider != "ibm" && provider != "qwen")) {
        std::cerr << "Unknown platform or provider\n";
        return 2;
    }
    // Only enumerated ASCII values are interpolated, not arbitrary user text.
    std::cout << R"({"version":"0.1","language":"en","vocabulary":"BEW","platform":")"
              << platform << R"(","provider":")" << provider
              << R"(","question":"Explain module, node and evidence in short words.","evidence_status":"synthetic_example","sources":[],"continuity":[true,false,true],"human_review":"pending"})"
              << '\n';
    return 0;
}
