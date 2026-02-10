from .reflection_agent.main import reflection_main
from .writting_agent.main import writing_main
from .appraisal_agent.main import appraisal_agent


def main():
    reflection = reflection_main()
    print(reflection)
    email = writing_main(reflection)
    print(email)
    appraisal = appraisal_agent(email)
    print(appraisal)