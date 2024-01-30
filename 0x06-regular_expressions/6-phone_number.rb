#!/usr/bin/env ruby
# Ruby script that accepts one argument and # pass it to a regular expression.
# must match a 10 digit phone number.
puts ARGV[0].scan(/^4155049898$/).join
