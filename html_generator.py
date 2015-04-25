# Function to create the top part of the lesson HTML 
def generate_lesson_box(lesson_title):
	html_lesson_box = '''
<div class="lesson-box">
	<div class="lesson-box-title"><h2>''' + lesson_title + '''</h2></div>
	<div class="lesson-box-content">'''
	return html_lesson_box

# Function to generate a single concept block
def generate_html_concept(concept_title, concept_description):
	html_concept_title = '''
		<h3>''' + concept_title + '''</h3>'''
	html_concept_description = '''
		<p>
		   ''' + concept_description + '''
		</p>
		<hr>'''
	
	html_concept = html_concept_title + html_concept_description
	return html_concept

# Variable to add the bottom of the html code at the end
closing_html = '''
	</div>
    <div class="lesson-box-bottom">
      	<p>
           <a href="#top">Back to Top</a>
      	</p>
	</div>
</div>'''

	
# Function to generate concepts stored in list
def generate_multiple_concepts(concept):
	concept_title = concept[0]
	concept_description = concept[1]
	return generate_html_concept(concept_title, concept_description)

concept_list = 	['Lesson 3: Programming and Computer Science', 
				["Programming as a Language", "Everything that a computer executes is done through a program."], 
				["Strings and Variables", "Variables are used to define and contain values"], 
				["Functions", '<em>Functions</em> process <em>input</em> and produce an <em>output</em>.']]	

# Function to put togheter all concepts plus begining and end HTML
def generate_html(list_of_concepts):
	if len(list_of_concepts) == 0:
		return 'No Data stored'
	else:
		lesson_box = generate_lesson_box(list_of_concepts[0])
		for concept in list_of_concepts[1:]:
			concept_box = generate_multiple_concepts(concept)
			lesson_box = lesson_box + concept_box
		all_concepts = lesson_box + closing_html 
		return all_concepts 




print generate_html(concept_list)

