<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">MACHINE_CODING</h1>
</p>
<p align="center">
    <em>Unleash the code, power up your projects!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/commit-activity/m/sharanreddy99/machine_coding" alt="last-commit">
	<img src="https://img.shields.io/github/created-at/sharanreddy99/machine_coding" alt="created_at">
   <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/sharanreddy99/machine_coding">
   <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/sharanreddy99/machine_coding">
   <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/sharanreddy99/machine_coding">

</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
</details>
<hr>

##  Overview

The machine_coding project encompasses a diverse set of engaging text-based games, including Snake and Ladder, Tic-Tac-Toe, 2048, and a Parking Lot simulator. Each game offers unique gameplay experiences while showcasing core functionalities like player movement, board interactions, and victory conditions. The project's value lies in providing users with customizable gaming environments that enhance strategic thinking and entertainment. Additionally, functionalities such as dynamic board creation, user input validation, and game progression tracking contribute to a seamless gaming experience.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project architecture includes various games like Snake and Ladder, Tic-Tac-Toe, Parking Lot, 2048. Each game has its own set of functionalities and rules, implemented in different Python scripts. The architecture is modular, allowing easy addition of new games. |
| 🔩 | **Code Quality**  | The codebase follows Python best practices, with well-structured and readable code. It includes proper variable naming conventions, code indentation, and comments for clarity. The codebase demonstrates good code quality and style. |
| 📄 | **Documentation** | The project provides detailed documentation for each game, explaining the functionalities, rules, and usage. The documentation covers the setup instructions, gameplay rules, and code structure, enhancing the overall understanding and ease of use for developers. |
| 🔌 | **Integrations**  | The key integrations include Python as the primary programming language and external dependencies like 'py' for certain functionalities. The project relies on standard Python libraries for core functionalities, ensuring compatibility and stability. |
| 🧩 | **Modularity**    | The codebase exhibits modularity, with separate scripts for different games and distinct functionalities within each game. This modular design enables easy maintenance, scalability, and reusability of code components across different games. |
| 🧪 | **Testing**       | The project uses test scripts like 'test_snake.py' and 'test_dice.py' to ensure proper functionality and validate different game scenarios. It demonstrates a commitment to testing practices, enhancing code reliability and robustness. |
| ⚡️  | **Performance**   | The project focuses on providing efficient gameplay experiences, with optimized algorithms for game logic and board operations. It efficiently manages player movements, dice rolls, and game states, ensuring smooth performance and minimal resource usage. |
| 🛡️ | **Security**      | While the provided details do not explicitly mention security measures, the codebase can implement access control mechanisms, input validation checks, and data protection strategies to enhance security. Strong coding practices can further strengthen data security. |
| 📦 | **Dependencies**  | The project relies on standard Python libraries and dependencies for core functionalities. External libraries like 'py' and basic Python packages support different aspects of the games, contributing to the overall functionality and feature richness. |
| 🚀 | **Scalability**   | The modular design of the project, along with the use of Python's dynamic capabilities, allows for easy scalability to handle increased traffic and load. The codebase can accommodate additional games or enhanced features with minimal effort, showcasing scalability potential. |

---

##  Repository Structure

```sh
└── machine_coding/
    ├── 2048.py
    ├── README.md
    ├── Snake Game
    │   ├── constants.py
    │   ├── dice.py
    │   ├── game.py
    │   ├── input.py
    │   ├── main.py
    │   ├── test_dice.py
    │   └── validation.py
    ├── parkinglot.py
    ├── snakeandladder.py
    ├── test_snake.py
    └── tic-tac-toe.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                             |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                 |
| [test_snake.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/test_snake.py)         | Improve test coverage for Snake and Ladder game by simulating user input scenarios. Check board creation and player initialization functions with different board configurations.                                                                                                   |
| [parkinglot.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/parkinglot.py)         | Creates parking lots with configurable floors and slots, allocates slots based on vehicle types, generates tickets, and allows parking and unparking vehicles. Dynamically tracks free and occupied slots per vehicle type.                                                         |
| [tic-tac-toe.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/tic-tac-toe.py)       | Facilitates a customizable Tic-Tac-Toe game with player inputs for grid size, player names, and shapes. Supports multiple players and validates moves, ensuring an engaging gameplay experience. Features board initialization, move tracking, victory checks, and restart options. |
| [snakeandladder.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/snakeandladder.py) | Implements a Snake and Ladder board game with dynamic size, player movements, dice rolls, and auto-generated snakes/ladders. Manages player positions, wins, and turns. Facilitates interactive player input for game setup and progression within the parent repository.           |
| [2048.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/2048.py)                     | Generates and manages a 2048 game board.-Offers functions to initialize the board, move and merge tiles, check for game completion, add random tiles, and print the board state.                                                                                                    |

</details>

<details closed><summary>Snake Game</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                     |
| ---                                                                                                       | ---                                                                                                                                                                                                                         |
| [dice.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/Snake Game/dice.py)             | Enables rolling a dice with a limit on consecutive sixes. Facilitates generating dice rolls and checking if a player can roll again based on the result. Crucial for driving game dynamics in the Snake Games architecture. |
| [test_dice.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/Snake Game/test_dice.py)   | Tests functionality of Dice class for throwing and rolling dice within specified limits through a series of test cases ensuring accurate results and behavior validation.                                                   |
| [main.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/Snake Game/main.py)             | Implements and starts the Snake game.                                                                                                                                                                                       |
| [game.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/Snake Game/game.py)             | Implements a text-based Snake Game with player movement, dice rolling, and ladder/snake features. Handles player turns and position updates using a grid system, with victory conditions triggering player elimination.     |
| [input.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/Snake Game/input.py)           | Handles user input to set up a game board with customizable grid dimensions, objects, and players. Automates object creation if desired. Handy for initializing game parameters seamlessly.                                 |
| [validation.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/Snake Game/validation.py) | Validates and determines player movements in the Snake and Ladder game. Ensures correct positions for snakes and ladders, preventing invalid moves.核                                                                        |
| [constants.py](https://github.com/sharanreddy99/machine_coding.git/blob/master/Snake Game/constants.py)   | Defines constants and user prompts for the Snake Game. Ensures input validation, player interaction, and game messaging. Facilitates setup and gameplay in alignment with the parent repositorys architecture.              |

</details>

---

##  Getting Started

###  Installation
All you need is python

###  Usage

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/sharanreddy99/machine_coding.git/issues)**: Submit bugs found or log feature requests for the `machine_coding` project.
- **[Submit Pull Requests](https://github.com/sharanreddy99/machine_coding.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/sharanreddy99/machine_coding.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/sharanreddy99/machine_coding.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com/sharanreddy99/machine_coding.git/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=sharanreddy99/machine_coding">
   </a>
</p>
</details>
