only eng
fuck ai
make the code work -> optimize
create cool stuff. you write the code for it(and for money from it)
the ideal is the enemy of the good
fuck meta, fuck idols
# ///
# ///
# ///

# [before 01.02]resful api + php oop
# ---(commit)
# [x] user
#   [x] implement logout button(jwt HttpOnly cookie cleaner)
#   [x] implement redirect to login page if user not authorized
#   [x] implement login logic
#   [x] make login in db unique
#   [x] add backend and frontend validation in register
#     [x] backend(!mail, !login unique)
#     [x] frontend(!input empty, !equal password, !email check, !login check(3+), !password check(6+), !display if login or email already taken(from backend))
#   [x] add backend and frontend validation in login
#     [x] backend(!incorrect login or pass)
#     [x] frontend(!not empty, !incorrect login or pass)
# ---(commit)

# [x] emotions
#   [x] create add api(request -> db)
#   [x] implement create page
#     [x] implemet auto increase emotion_trigger input, then it filled
#     # [x]from form body to json body
#     [x] request to api in frontend side(save)
#   [x] create api that displaying all emotions(request -> all emotions in json)
#   [x] draw html based on an api response
#     [x] add emotion highlight based on selected color
#   [x] create api, that return only 1 emotion(request(id) -> emotion data)
#   [x] implement tap to open
#   [x] create edit page
#     [x] implement delete(api, request)
#     [x] implement update(api, request)
#     [x] delete confirmation pop up(cancel, delete), exit pop up(if edited)(cancel, don't save)
#       [x] addevenlistener on button -> create element(pop up) -> block all -> unlock after press cancel -> redirrect after confirmation
#   [x] add highlight in footer

# bug fix:
#   [x] password too short in login destroy form | i changed border color to 171717 instead of 222222
#   [x] swap from application/x-www-form-urlencoded form to json request(json request body -> api -> json output)
#   [x] fix register/login on phone(backend don't work) | /backend/api/auth/login.php insted of http://localhost:8080/backend/api/auth/login.php work
# ---(commit)

# [x] desires->projects->hypothesis->result->hypothesis->complete
#   [x] db
#     [x] desires: id, user_id, desire, is_active
#     [x] projects: id, user_id, desire_id, project, is_active
#     [x] iterations: id, user_id, project_id, iteration_type(result/hypothesis), iteration
#   [x] desires
#     [x] desires add 
#     [x] desires page
#     [x] edit, delete
#   [x] projetcs
#     [x] projects add
#       [x] implement back button(send ?id=x in js?) and in api when save check: does the user have desire with this id
#     [x] projects page
#     [x] edit, delete
#   [x] iterations
#     [x] iterations add
#       [x] get previous iteration. if type = 0(hypothesis) then type = 1(result). it type = 1: type = 0. if it empty: type = 0;
#     [x] iterations page
#       [x] for iterations: iteration(border blue(type == 0) or orange(type == 1)) + ↓
#     [x] iterations edit
# ---(commit)

# [] routines
#   [x] create routine
#     [x] i want: click on any place in input -> show calendar widget.(prohibit input). default day in calendar = today
#     [x] implement selector(every X day or week days)
#     [x] week selector(change background color and get value)
#     [x] check if routine text and routine result not null, focus
#     [x] create api
#   [] routines page
#     [] change of position by holding(in db too)
#   [] routines edit
#   [] timer(like coding -> timer start -> some actions on db)

# [] iteration edit only in last iteration
# [] add auth checker on all page
# [] elements load after page loads(fix it)

# [] swagger

# [] if have time - refactor code

# # typehints and code style is good
# # [] i want auto code style checker(like Flake8 in vscode python) best css practices, best js, best php
#     [] php cs fixer(only fix, don't need), php codesniffer(i need it)



# ///
# ///
# ///
# /// i don't want to finish this project. In February i start learn laravel.
# ///
# ///
# ///

# [x] add this to github(2 files)

# [x] let's test will I able to change this file from phone and then merge it 

# code helper(decomposition, projects, timer)
# life helper(routine, notes)								 
# projects(this file + done or not), routine(habitica, calendar, how many days until next), notes(google keep)
# [before 01.03] laravel project(php, blade, bootstrap, mysql, js)
#     # [x] laracast 30 days course
# 	# [x] create project with starterpack
# 	# [x] implement authorization
# 	# [x] connect bootstrap
# 	[] project page
# 		# [x] draw, drop a link - https://excalidraw.com/#json=65H576GEXSSBEZkfGkrR8,tllM6RzpJrHxA2ofmi3zaA
# 		# [x] projects: create model, migration(id, user_id, is_done, name, comments), controller, route 
# 		# [x] create small register and login
# 		# 	[x] add frontend validation from course
# 		# 	[x] log in failure messages
# 		# [x] auth check
# 		# [x] index page without tasks
# 		# [x] create page(name, some comments)
# 		# 	[x] save to db
# 		# 	[x] validation
# 		# [x] index page full
# 		# 	[x] hover effect
# 		# 	[x] test long name, comment(copy from habitica) 
# 			# [x] clickable to projects/{id}/edit
# 		[] edit/show page
# 			# [x] get (name, comment) from db by id in url
# 			# 	[x] implement logic: the user has access only to his own projects(gate?)
# 			# [x] fix: i can see projects which i did not create
# 			# [x] create tasks(migration, model, controller, policy)(project_id, is_done, task_text, tabs)
# 				# [x] implement logic: if a project with tasks is deleted - delete the tasks https://www.youtube.com/watch?v=x1UCiE0hZiw&list=PL3VM-unCzF8hy47mt9-chowaHNjfkuEVz&index=12
# 		# [x] create github
# 			# [x] task block
# 				# [x] implement create button
# 				# [x] fix the low position of the button
# 			[] update(save button) https://www.youtube.com/watch?v=syx1tWSZbL8&list=PL3VM-unCzF8hy47mt9-chowaHNjfkuEVz&index=18
# 				# [x] name, comment
# 				[] tasks
# 			[] delete
# 	# [x] nav page
# 	# 	[x] highlight active page
# 		# [x] fix absolute(margin or stmh like this)	
# 	[] timer page
# 		[] time input(h, m, s)
# 		[] timer 
# FUCK BOOTSTRAP, FUCK BLADE

[before 01.04] laravel api + docker + mysql + vue spa = a project to help coders
	[] vue tutorial
	[] black/white? like vue docs think about design
	[] i can delete tailwind from starter kit auth and rewrite it later with my styling
	[] decomposition(this file)(literally copy, but 1 space at the beginning = tab(i can't write in it) and clikable checkbox)
	[] timer
	[?] routines(habitica), why i do this?
	[?] notes?
	[] get feedback(users, coders(laravel chat?))




























[01.04] ask for resume advice, start learning the theory for interviews
[] anime site collab
[before 01.06] job(mysql, php, laravel, oop, (html css js bootstrap tailwind, vue), rest api, docker, github)
[?] tg bot for $$$?
				
