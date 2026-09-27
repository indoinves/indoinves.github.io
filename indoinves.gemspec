Gem::Specification.new do |spec|
  spec.name          = "indoinves"
  spec.version       = "1.0.0"
  spec.authors       = ["IndoInves Team"]
  spec.email         = ["support@indoinves.github.io"]

  spec.summary       = "Platform Pintar Investasi, Keuangan, dan Kumpulan Tools Finansial Modern"
  spec.homepage      = "https://indoinves.github.io/"
  spec.license       = "MIT"

  spec.files         = Dir.chdir(File.expand_path(__dir__)) do
    `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  end
  
  spec.require_paths = ["."]
end
