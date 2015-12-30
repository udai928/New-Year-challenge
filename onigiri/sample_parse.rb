require 'open-uri'
require 'nokogiri'

url = 'https://www.microad.co.jp'

charset = nil
html = open(url) do |f|
  charset = f.charset
  f.read
end

doc = Nokogiri::HTML.parse(html, nil, charset)

doc.css('a').each do |anchor|
  if anchor[:href].index("http") then
    p anchor[:href]
  else
    p url + anchor[:href]
  end
end
