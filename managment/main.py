import datetime
from redminelib import Redmine
from settings import api_token, issues, users

tracker_id = 4
status_id = 1
priority_id = 4
url = 'https://projects.osinit.com'
project_id = 'os-internal-hr-internship-py-js-2019'
redmine = Redmine(url, key=api_token)


def create_issues(issue_id):
    """
    Список пользователей users должен содержать словари следующего формата:
    users = [
        {'id': 1, 'name': 'Иван Иванов'},
    ]
    Список задач должен следующего формата:
    issues = [
        {'subject': 'Задача', 'start_date': datetime.date(2019, 4, 29), assign_to: 130},
    ]
    :param issue_id: индекс в списке задач
    :return:
    """
    issue = issues[issue_id]
    due_date = issue['start_date'] + datetime.timedelta(days=7)
    base_issue_kwargs = dict(
        project_id=project_id,
        tracker_id=tracker_id,
        status_id=status_id,
        priority_id=priority_id,
        due_date=due_date,
        start_date=issue['start_date'],
    )
    try:
        base_issue = redmine.issue.create(
            assigned_to_id=issues['assign_to'],
            subject=issue['subject'],
            **base_issue_kwargs,
        )
    except Exception as e:
        # Наш redmine отдает ответ с ошибкой, поэтому просто игнорируем
        print(f'For {issues["assign_to"]}, created with exception {e}')
    for user in users:
        # TODO: сделать проверку, что такого задания еще нет.
        try:
            redmine.issue.create(
                assigned_to_id=user['id'],
                parent_issue_id=base_issue.id,
                subject='{}: {}'.format(issue['subject'], user['name']),
                **base_issue_kwargs,
            )
        except Exception as e:
            # Наш redmine отдает ответ с ошибкой, поэтому просто игнорируем
            print(f'For {user["name"]}, created with exception {e}')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('issue_id', type=int)
    args = parser.parse_args()
    create_issues(args.issue_id)
