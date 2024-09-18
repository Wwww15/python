from git.repo import Repo


repo_path = "C:/Users/JD/Desktop/project/test_code/python"
repo_url = "https://github.com/Wwww15/python.git"
repo = Repo.clone_from(repo_url, repo_path)

tag_name = "v1.0.5"
tag_message = "This is an annotated tag"


repo.git.checkout(tag_name)
message = repo.tag(tag_name).object.message
print(message)


