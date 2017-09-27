require 'csv'

def csvparse(file)
  config = CSV.read(file)
  list = []
  config.each do |c|
    1.upto(6) do |i|
      if !c[i].nil?
        unless c[i].match(/N/)
          list.push(c[i])
        end
      end
    end
  end

  counts = Hash.new 0

  list.each do |word|
    counts[word] += 1
  end

  sorted_hash = counts.sort_by {|_key, value| -value}.to_h
  puts sorted_hash.keys.join(" ")
end

puts('-----------5/40-----------')
csvparse('540.csv')
puts('-----------6/49-----------')
csvparse('loto649.csv')
