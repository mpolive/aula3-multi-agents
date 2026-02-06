from .reflection_agent.main import reflection_main
from .writting_agent.main import writting_main
from .appraisal_agent.main import appraisal_agent


def main():
    reflection = reflection_main()
    email = writting_main(reflection)
    print(appraisal_agent(email))

if __name__ == "__main__":
    main()