#!/usr/bin/env python
# -*- coding:utf-8 -*-

'database'

__Author__='Wang'


import sqlite3


class MyDatabase(object):
	def __init__(self):

		self.conn = sqlite3.connect('test.db')
		cursor = self.conn.cursor()
		cursor.execute('create table if not exists user (id varchar(20) primary key, address varchar(30))')
		cursor.close()
		print 'database start...'

	def add(self, id_, addr_):
		cursor = self.conn.cursor()
		cursor.execute('insert into user (id, address) values (?, ?)' , (id_, addr_))
		cursor.close()
		self.conn.commit()
		cursor.close()

	def update(self, id_, addr_):
		cursor = self.conn.cursor()
		cursor.execute('update user set address=? where id = ?' , (addr_, id_))
		cursor.close()
		self.conn.commit()

	def  query(self):
		cursor = self.conn.cursor()

		cursor.execute('select * from user')

		values = cursor.fetchall()

		#print len(values)

		cursor.close()

		return values

	def __del__(self):
		self.conn.close()
		print 'database closed!'


if __name__=='__main__':
	db = MyDatabase()
	#db.add('3', '123')
	#db.update('3','122')
	db.query()