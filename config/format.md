# Config file format
Config files describe the setting the character is created in. They are written in JSON as a dictionary. An example file is provided as `example.json`.

**Note:** lot of this file is colored by RPG logic. If you are unfamiliar with it, it may be slightly confusing. As this is a character creator, a tool used by someone advanced in RPGs, I put as much explanation as it was absolutely necessary.

## Sections

*Note:* "conditionally optional entry" in case of Attributes and Skills means that at least one of those sections must be defined. It does not matter which one.

### Basic
_This is a mandatory entry_

This section is responsible for listing all the other sections in a format of a dictionary with section name as the key and listed fields as content. All fields are optional, if not provided, default values are used.

- `progression` - `string` - type of progression
    - `constant` - the cost is the same for every level: 1, 1, 1, 1, 1
    - `linear` - the cost increases linearly: 1, 2, 3, 4, 5; this is the default option 
    - `quadratic` - the cost increases quadratically: 1, 4, 9, 16, 25
    - `fibonacci` - the cost is a Fibonacci sequence: 1, 2, 3, 5, 8
- `start` - `int` - start of the sequence; for 1, no positions are skipped, for 2 first one is skipped, etc.; 1 is the default value
- `multiplier` - `int` - linear multiplier for all costs; 1 is the default value
- `limit` - `int` - maximum possible value to be developed; 10 is the default value
- `unit` - `string` - type of points used for this value
    - `P` - generic Points; this is the default option
    - `AP` - Attribute Points
    - `SP` - Skill Points
    - `TP` - Trait Points
    - `POW` - Powers
    - `DEV` - Developments

### Attributes
_This is a conditionally optional entry_

Attributes are major, hard-to-develop dice contributors. They are assumed to be unique: there is no point in having two Intellect scores.

#### Fields

##### Mandatory
- `identifier` - `string` - short code 
- `name` - `string` - proper name

##### Optional
- `description` - array of `string`, each entry containing a line of description

### Skills
_This is a conditionally optional entry_

Skills are minor, easy-to-develop dice contributors. They are assumed to be unique.

#### Fields

#### Mandatory
- `identifier` - `string` - short code 
- `name` - `string` - proper name

#### Optional
- `description` - array of `string`, each entry containing a line of description

#### ToDo
- group skills for Art, Craft, etc. things
- specialization

### Traits
_This is an optional entry_

Traits are "miscellaneous" things - advantages, disadvantages, and similar details. They are assumed to be unique.

#### Fields

##### Mandatory
- `identifier` - `string` - short code 
- `name` - `string` - proper name

##### Optional
- `description` - array of `string`, each entry containing a line of description

### Powers
_This is an optional entry_

Powers are specific abilities. They are assumed to be unique.

#### Fields

##### Mandatory
- `identifier` - `string` - short code 
- `name` - `string` - proper name

##### Optional
- `description` - array of `string`, each entry containing a line of description

### Developments
_This is an optional entry_

Developments are a list of possible steps for developing the character. They are not supposed to be unique.

#### Fields

##### Mandatory
- `identifier` - `string` - short code
- `name` - `string` - proper name
- `provides` - `int` - amount of points provided
- `unit` - `?` - type of points provided

##### Optional
- `description` - array of `string`, each entry containing a line of description

#### ToDo
Roll units and values of costs into one object? 

## Intended structure
- Config file as the base, describing setting; it would be delivered with the rulebook
- [optional] Setup file in the middle, describing epic-specific changes and settings; contains reference to config file it is based on; it would be delivered by the Game Master or as part of a setting-specific supplement 
- Template file for the specific case, describing specific values the character should be built with; contains reference to setup file it is based on or config file if no setup file is used; delivered by the Game Master, based on existing templates 