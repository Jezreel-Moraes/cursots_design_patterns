from classes.soccer_crowd import AdversarySupporterTeam, SupporterTeam
from classes.soccer_team_subject import SoccerTeam


def main():
    team = SoccerTeam('Real Madrid')
    supporter = SupporterTeam()
    adversary = AdversarySupporterTeam()

    team.subscribe(supporter, adversary)
    print()
    team.score_goal()
    print()
    team.concede_goal()
    print()

    team.unsubscribe(supporter)
    print()
    team.score_goal()
    print()
    team.concede_goal()
    print()

    team.unsubscribe(adversary)
    print()
    team.score_goal()
    print()
    team.concede_goal()
    print()


if __name__ == '__main__':
    main()
