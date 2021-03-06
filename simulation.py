# Copyright (c) 2015 
# Author: Xerxes Wu
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from opturtle_v1 import *
from strategy import *
from utils import *

if __name__ == '__main__':
	data = read_data (sys.argv)
	turtle = OPTurtle (data)
	turtle.setup()
	create_strategy (turtle, EQUITY)
	# bo_dict = turtle.bo_dict

	# for key, value in bo_dict.items():
	# 	print key
	# 	print "Entry date: {0}, Entry price: {1}, Strategy type: {2}, Is loser: {3}".format (value.entry_date, value.entry_price, value.strategy_type, value.is_loser)
	# tr_list = turtle.tr_list
	# n_list = turtle.n_list
	# x = range (len (n_list))
	# plt.plot(x, n_list, color='r')
	# y = range (len (tr_list))
	# plt.plot(y, tr_list, color='g')
	# x = range (len (price_list))
	# plt.plot(x, price_list, color='b')
	# plt.show()
