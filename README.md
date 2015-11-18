# docker12factor
Code companion to a presentation on twelve-factor app best practices, using Docker


1. Codebase:
Do:
	- Commit early, commit often. Preferably to git/hg
Don’t:
	- Shuffle code around on usb’s, dropbox, etc… EVER. You can have private repos for free on GitLab

Why?
Good version control habits will save you THOUSANDS of hours of work over your career. Your co-workers will love and appreciate your atomic commits and tidy commit messages. Even some non-programmers (eg. designers) today are expected to have good VCS habits, so as a CS grad this is something you should know.

2. Dependencies
Do:
	- One place for ALL your dependencies

Don’t:
	- Don’t ever rely on a package or a library being available.
	- Shell out to the system during runtime to call an external dependency you have not defined/installed.

Why?
As soon as more than 1 person is working on a codebase, if you don’t list all your dependencies you are making other people’s lives miserable. This includes not just developers, but sysadmins as well.

3. Config
Do:
	- Store configuration variables as environment variables
	- Or at least store them separately from code

Don’t:
	- Don’t store system paths as hardcoded strings in code
	- Don’t let API keys and secrets end up getting checked into version control

Why?
Code cleanliness, protecting secrets, and enabling everyone to work on the same version of the code, while only changing some config files or variables.

4. Storage and Services
Do:
	- Encapsulate your state in the database
	- Treat backing services as separate services altogether

Don’t:
	- Don’t store state in your app, except in your backing services, such as a database.
	- Don’t use a different backing service in development and production. Eg. using sqlite locally and postgres on prod.

Why?
See 10. - Dev/Prod parity

5. Silo off your production environments
Do:
	- Develop locally, commit, the deploy

Don’t:
	- Change code in production.

Why?
If you’re changing code in production, you are introducing state into the environment, which is then lost. This can make reproducing bugs extremely difficult.

6. Processes
Do:
	- Have separate processes for web, db, background tasks, etc…

Don’t:
	- Spawn worker queues or other jobs from your main HTTP process.

Why?
Scalability.

7. Bind to ports
Do:
	- Expose your services through ports

Don’t:
	- Piggyback your services off other processes - eg. Apache mods or Tomcat servlet containers

Why?
Your processes should be self-contained. This helps hugely with scalability.

8. Concurrency
Do:
	- Spawn new processes of a given type when you encounter a bottleneck.

9. Disposability
Do:
	- Occasionally kill your processes.

Don’t:
	- Fear killing your processes. If you feel anxious about killing your web process, there’s probably something you’re doing wrong.

Why?
It’s a good sanity check to make sure you’re not introducing state in multiple places. Also good for scalability and redundancy.

10. Dev/Prod Parity
Do:
	- Try to make your development environment as close as humanly possible to your prod environment.

11. Logs
Do:
 - Log to stdout

Don’t:
	- Log to filesystem

Why?
If you’re logging to disk, you’re introducing state.

12. Admin
Do:
	- Run one-off tasks as separate processes


