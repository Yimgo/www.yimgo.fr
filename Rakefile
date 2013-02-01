require 'sass'
require 'haml'

task :default => :build

desc 'Build site'
task :build do
  sassengine = Sass::Engine.for_file("css/style.sass", :syntax => :sass, :style => :compressed)
  css = sassengine.render()

  File.open("_site/style.css", "w") { |f| f.write(css) }

  haml = IO.read("index.haml")
  hamlengine = Haml::Engine.new(haml)
  html = hamlengine.render()

  File.open("_site/index.html", "w") { |f| f.write(html) }
end
