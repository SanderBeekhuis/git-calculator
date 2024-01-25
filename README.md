# Calculator
Small repo used for demo-ing how branches work with git. 

## Getting Started
1. Install poetry
2. Run `poetry install` to install dependencies
3. Run `poetry shell` to activate virtual environment
4. Run `pytest` to run tests and `flake8` to lint

## Demo 

### Een PR maken - Subtraction
Maak een PR waar we aftrekken toevoegen.

- Voorbeeld: Schrijf extra functionaliteit.
- Voorbeeld: PR voor deze functionaliteit
- Wacht op pijplijn en merge


### Tweede/oude PR - Multi-arg add
- Git history laten zien 

[Make add work for any number of arguments](https://github.com/SanderBeekhuis/calculator/pull/3)

- Laat zien hoe Git automatisch merged
- Kantekening: Na een goede merge hoeft de code niet per se logisch te zijn. Het is raar dat onze function signatures nu
niet matchen.  

### Merge conflict - Multiplication
- Opnieuw git history laten zien

[Add multiplication method](https://github.com/SanderBeekhuis/calculator/pull/4)
- Laat zien dat de pipeline faalt, deze eerst fixen door onze tests te fixen

- Soms kan Git niet automatisch mergen
- Voorbeeld: Merge conflict met andere nieuwe functionaliteit
- Laat zien hoe je merge conflicts resolved. 


## Exercises
- Maak een pull request voor 
   - division
   - power
   - multi-arg multiplication

- Review elkaars pull requests.
   - Probeer een comment te maken. (Al is het maar voor de vorm)
   - Los de comments op
   - Krijg approval
   - Merge de pull request
