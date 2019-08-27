from bs4 import BeautifulSoup

class Converters:
  def convertStyleToClass(self, html):
    """
    Take a string of html content, find all the tags with a style
    attribute and convert them to classes.
    
    Args:
      html:

    Returns:
      cssFileContent: a string containing the new css classes in css format
      soup.prettify(): updated html with new classes

    """

    soup = BeautifulSoup(html, 'html.parser')
    cssFileContent = ""
    style_classes = {}
    class_num = 1

    # iterate over all the tags that have the style attribute
    for tag in soup.findAll("", {'style': True}):
      # retrieve the style and class value
      styles = tag['style'] if tag.has_attr('style') else None
      classes = tag['class'] if tag.has_attr('class') else None

      styles = styles.strip().split(";")
      className = "newClass" + str(class_num)

      # remove all spaces and order by styles by property name
      for j, style in enumerate(styles):
        property_name_val = style.split(":")
        if len(property_name_val) == 2:
          # remove spaces before and after
          styles[j] = property_name_val[0].strip() + ":" + property_name_val[1].strip()

      # sort the styles so that we can look for duplicate collections
      # of styles
      styles.sort(key=lambda s: s.split(':')[0])

      # if same group of styles exists, use its new class name
      # otherwise create new class
      style_val = ";".join(styles)
      if style_val in style_classes:
        className = style_classes[style_val]
      else:
        style_classes[style_val] = className
        class_num += 1

        # create the css class and to the final css file content
        cssFileContent += "." + className + " {"
        for style in styles:
          if style != '':
            cssFileContent += "\n\t" + style + ","

        cssFileContent += "\n" + "}" + "\n\n"

      # remove style and add new class name
      tag['class'] = tag['class'] + [className] if classes else className
      del tag['style']

    return cssFileContent, soup.prettify()