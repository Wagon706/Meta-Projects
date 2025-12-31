try:
	import pymysql
	pymysql.install_as_MySQLdb()
except Exception:
	# Safe no-op if PyMySQL isn't installed yet
	pass

