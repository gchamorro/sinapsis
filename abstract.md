# SINAPSIS

## Work model

* Code is managed via github, so can be downloaded and commited no matter the host or location of coding. An account is created both in github an gmail.
* Commented and documented every step.

## Models

### Person

```python
class Person(models.Model):
    DNI = 'DN'
    LIBRETA_CIVICA = 'LC'
    LIBRETA_ENROLAMIENTO = 'LE'
    PASAPORTE = 'PA'
    UNDEFINED = 'UN'
    DOCUMENT_CHOICES = (
        (DNI, 'Documento único'),
        (LIBRETA_CIVICA, 'Libreta cívica'),
        (LIBRETA_ENROLAMIENTO, 'Libreta enrolamiento'),
        (PASAPORTE, 'Pasaporte'),
        (UNDEFINED, 'No definido'),
    )
    first_names=models.CharField(
        'Nombres',
        max_length=100,
        validators=[RegexValidator(u'^[a-zA-ZñÑüÜáéíóúÁÉÍÓÚ\'\s\.]*$', 'Sólo se permiten caracteres al fabéticos')],
    )
    last_names=models.CharField(
        'Apellidos',
        max_length=100,
        validators=[RegexValidator(u'^[a-zA-ZñÑüÜáéíóúÁÉÍÓÚ\'\s\.]*$', 'Sólo se permiten caracteres al fabéticos')],
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=DOCUMENT_CHOICES,
        default=DNI
    )
    document_number = models.CharField(
        'Nro. de Documento',
        max_length=11,
        validators=[RegexValidator('\d\d\d\d\d\d\d\d', 'El nro debe constar de ocho dígitos sin espacios o puntos')],
    )
    cuil = models.CharField(
        'Cuil',
        max_length = 11,
        blank = True,
        default = '',
        validators = [RegexValidator('\d\d\d\d\d\d\d\d', 'El nro debe constar de once dígitos sin espacios o puntos')],
    )
    birthday = models.DateField(
        'Fecha de nacimiento',
        null = True,
        blank = True,
    )    
    
    def __unicode__(self):
        return self.last_names.upper() + ', ' + self.first_names.title()
    
    def _get_full_name(self):
        return '%s, %s' % (self.last_names.upper(), self.first_names.title())
    
    def _calculate_age(self):
        today = date.today()
        age = 'no birth date defined!'
        if self.birth_date:
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    def validate_names(self, value):
        validator = [RegexValidator(u'^[a-zA-ZñÑüÜáéíóúÁÉÍÓÚ\'\s\.]*$', 'Sólo se permiten caracteres al fabéticos')],
        pass
        
    full_name = property(_get_full_name)
    age = property(_calculate_age)
    
    class Meta:
        ordering = ['last_names']
        verbose_name="Persona"
        verbose_name_plural="People" 
``` 

#### Fields

##### last_names

* Spanish readable human name **'Apellidos'**
* max_length=**100?**
	What is the recommended length for this kind of fields?
* validators
	Only alphabetic characters, including **'**, and spanish accented characteres

##### first_names
    
## UX

### 

### Development

* Define basic interfaces (some CRUD) to apply globally, followin some (simple?) generic steps. For example, what and how is isplayed on index pages (despite the fact that it's not going to be on production). The most basic is a list and some action commands maybe.

* Define structurally every view, without forcing specific html, css, javascript on it. It maybe even interchangeable. According to the design then start working on the html snippets or helpers, maybe with no app interactio (pure html).

* Define some helper interfaces for common tasks, example of it is messages.

* Use specific name variables for specific layouts when passing to templates, so an error will raise if not meant for that layout

### Production

### Bootstrap