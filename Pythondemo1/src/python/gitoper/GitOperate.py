import git

repo = git.Repo.init('D:/Study/Python/python')

commit = repo.head.commit
tag_name = "v1.0.5"
tag_message = "This is an annotated tag"

repo.create_tag(tag_name, ref=commit, message=tag_message)
origin = repo.remote(name='origin')
origin.push(tag_name)
