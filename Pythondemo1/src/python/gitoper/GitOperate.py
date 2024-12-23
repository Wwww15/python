import shutil

from git.repo import Repo


repo = Repo.init("/home/git/python")
# repo_path = "/home/git/python"
# repo_url = "git@github.com:Wwww15/python.git"
# repo = Repo.clone_from(repo_url, repo_path)
#
# tag_name = "v1.0.5"
# tag_message = "This is an annotated tag"
#
#
# repo.git.checkout(tag_name)
# message = repo.tag(tag_name).object.message
# print(message)

# repo = Repo.init("/home/git/python")
#
repo_git = repo.git
src_path = "/home/temp/test1.py"
dst_path = "/home/git/python/Pythondemo1/src/python/test/"
shutil.copy(src_path,dst_path)
index = repo.index
index.add(["/home/git/python/Pythondemo1/src/python/test/test1.py"])

index.commit("add test1.py")
repo_remote = repo.remote()
repo_remote.set_url("git@github.com:Wwww15/python.git")
repo_remote.push()
