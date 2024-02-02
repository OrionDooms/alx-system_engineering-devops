#!/usr/bin/env ruby
# Ruby script that accepts one argument and
# pass it to a regular expression
# The script output: [SENDER],[RECEIVER],[FLAGS]    
puts ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flages:(.*?)\]/).flatten.compact.join(',')
