all
exclude_rule 'MD002'
exclude_rule 'MD033'
exclude_rule 'MD041'
rule 'MD004', :style => :dash
rule 'MD007', :indent => 4
rule 'MD013', :ignore_code_blocks => true, :tables => false
rule "MD024", :allow_different_nesting => true
rule 'MD029', :style => :ordered
