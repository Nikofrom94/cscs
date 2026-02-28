from typing import List
from typing import Optional
from sqlalchemy.types import String,Text,Integer,Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Table

class Base(DeclarativeBase):
    pass

class Language(Base):
    __tablename__ = "csqt_language"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    ab_langs: Mapped["CSAbilityLang"] = relationship(back_populates="language")
    focus_langs: Mapped["CSFocusLang"] = relationship(back_populates="language")
    descriptorcharacteristic_langs: Mapped["CSDescriptorCharacteristicLang"] = relationship(back_populates="language")
    flavor_langs: Mapped["CSFlavorLang"] = relationship(back_populates="language")
    charactertype_langs: Mapped["CSCharacterTypeLang"] = relationship(back_populates="language")
    cypher_langs: Mapped["CSCypherLang"] = relationship(back_populates="language")
    descriptor_langs: Mapped["CSDescriptorLang"] = relationship(back_populates="language")

# association table between tables abilities and focusabilities
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
focusabilities_abilities_table = Table(
    "csqt_focusabilities_abilities",
    Base.metadata,
    Column("focusabilities_id", ForeignKey("csqt_focusabilities.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
# association table between tables abilities and focusabilities for abilities to choose
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
focusabilities_abilities_to_choose_table = Table(
    "csqt_focusabilities_abilities_to_choose",
    Base.metadata,
    Column("focusabilities_id", ForeignKey("csqt_focusabilities.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
# association table between tables flavor and abilities for tier1
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
flavor_abilities_tier1_table = Table(
    "csqt_flavor_abilities_tier1",
    Base.metadata,
    Column("flavor_id", ForeignKey("csqt_flavor.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)

# association table between tables flavor and abilities for tier2
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
flavor_abilities_tier2_table = Table(
    "csqt_flavor_abilities_tier2",
    Base.metadata,
    Column("flavor_id", ForeignKey("csqt_flavor.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)

# association table between tables flavor and abilities for tier3
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
flavor_abilities_tier3_table = Table(
    "csqt_flavor_abilities_tier3",
    Base.metadata,
    Column("flavor_id", ForeignKey("csqt_flavor.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)

# association table between tables flavor and abilities for tier4
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
flavor_abilities_tier4_table = Table(
    "csqt_flavor_abilities_tier4",
    Base.metadata,
    Column("flavor_id", ForeignKey("csqt_flavor.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)

# association table between tables flavor and abilities for tier5
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
flavor_abilities_tier5_table = Table(
    "csqt_flavor_abilities_tier5",
    Base.metadata,
    Column("flavor_id", ForeignKey("csqt_flavor.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)

# association table between tables flavor and abilities for tier6
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
flavor_abilities_tier6_table = Table(
    "csqt_flavor_abilities_tier6",
    Base.metadata,
    Column("flavor_id", ForeignKey("csqt_flavor.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)


# association table between tables flavor and abilities for tier6
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
type_abilities_tier1_table = Table(
    "csqt_charactertype_abilities_tier1",
    Base.metadata,
    Column("charactertype_id", ForeignKey("csqt_charactertype.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)

# association table between tables charactertype and abilities for tier1 to 6
type_abilities_tier2_table = Table(
    "csqt_charactertype_abilities_tier2",
    Base.metadata,
    Column("charactertype_id", ForeignKey("csqt_charactertype.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
type_abilities_tier3_table = Table(
    "csqt_charactertype_abilities_tier3",
    Base.metadata,
    Column("charactertype_id", ForeignKey("csqt_charactertype.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
type_abilities_tier4_table = Table(
    "csqt_charactertype_abilities_tier4",
    Base.metadata,
    Column("charactertype_id", ForeignKey("csqt_charactertype.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
type_abilities_tier5_table = Table(
    "csqt_charactertype_abilities_tier5",
    Base.metadata,
    Column("charactertype_id", ForeignKey("csqt_charactertype.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
type_abilities_tier6_table = Table(
    "csqt_charactertype_abilities_tier6",
    Base.metadata,
    Column("charactertype_id", ForeignKey("csqt_charactertype.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
character_flavor_table = Table(
    "csqt_character_flavors",
    Base.metadata,
    Column("character_id", ForeignKey("csqt_character.id")),
    Column("flavor_id", ForeignKey("csqt_flavor.id")),
)
character_descriptor_table = Table(
    "csqt_character_descriptors",
    Base.metadata,
    Column("character_id", ForeignKey("csqt_character.id")),
    Column("descriptor_id", ForeignKey("csqt_descriptor.id")),
)
character_cypher_table = Table(
    "csqt_character_cyphers",
    Base.metadata,
    Column("character_id", ForeignKey("csqt_character.id")),
    Column("cypher_id", ForeignKey("csqt_cypher.id")),
)
character_ability_table = Table(
    "csqt_character_abilities",
    Base.metadata,
    Column("character_id", ForeignKey("csqt_character.id")),
    Column("ability_id", ForeignKey("csqt_ability.id")),
)
descriptor_characteristics_table = Table(
    "csqt_descriptor_characteristics",
    Base.metadata,
    Column("descriptor_id", ForeignKey("csqt_descriptor.id")),
    Column("descriptorcharacteristic_id", ForeignKey("csqt_descriptorcharacteristic.id")),
)

class CSAbility(Base):
    __tablename__ = "csqt_ability"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cs_page: Mapped[str] = mapped_column(String(30))
    tier: Mapped[str] = mapped_column(String(1))
    locales: Mapped[List["CSAbilityLang"]] = relationship(back_populates="ability")
    focusabilities: Mapped[List["CSFocusAbilities"]] = relationship(
        secondary=focusabilities_abilities_table,
        back_populates="abilities"
        )
    focusabilities_to_choose: Mapped[List["CSFocusAbilities"]] = relationship(
        secondary=focusabilities_abilities_to_choose_table,
        back_populates="abilities_to_choose"
        )
    flavorabilities_rank1: Mapped[List["CSFlavor"]] = relationship(
        secondary=flavor_abilities_tier1_table,
        back_populates="abilities_rank1"
        ) 
    flavorabilities_rank2: Mapped[List["CSFlavor"]] = relationship(
        secondary=flavor_abilities_tier2_table,
        back_populates="abilities_rank2"
        )
    flavorabilities_rank3: Mapped[List["CSFlavor"]] = relationship(
        secondary=flavor_abilities_tier3_table,
        back_populates="abilities_rank3"
        )
    flavorabilities_rank4: Mapped[List["CSFlavor"]] = relationship(
        secondary=flavor_abilities_tier4_table,
        back_populates="abilities_rank4"
        )
    flavorabilities_rank5: Mapped[List["CSFlavor"]] = relationship(
        secondary=flavor_abilities_tier5_table,
        back_populates="abilities_rank5"
        )
    flavorabilities_rank6: Mapped[List["CSFlavor"]] = relationship(
        secondary=flavor_abilities_tier6_table,
        back_populates="abilities_rank6"
        )
    typeabilities_rank1: Mapped[List["CSCharacterType"]] = relationship(
        secondary=type_abilities_tier1_table,
        back_populates="abilities_rank1"
        ) 
    typeabilities_rank2: Mapped[List["CSCharacterType"]] = relationship(
        secondary=type_abilities_tier2_table,
        back_populates="abilities_rank2"
        ) 
    typeabilities_rank3: Mapped[List["CSCharacterType"]] = relationship(
        secondary=type_abilities_tier3_table,
        back_populates="abilities_rank3"
        ) 
    typeabilities_rank4: Mapped[List["CSCharacterType"]] = relationship(
        secondary=type_abilities_tier4_table,
        back_populates="abilities_rank4"
        ) 
    typeabilities_rank5: Mapped[List["CSCharacterType"]] = relationship(
        secondary=type_abilities_tier5_table,
        back_populates="abilities_rank5"
        ) 
    typeabilities_rank6: Mapped[List["CSCharacterType"]] = relationship(
        secondary=type_abilities_tier6_table,
        back_populates="abilities_rank6"
        ) 
    characters: Mapped[List["CSCharacter"]] = relationship(
        secondary=character_ability_table,
        back_populates="abilities"
        )
    
class CSAbilityLang(Base):
    __tablename__ = "csqt_abilitylang"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    stat: Mapped[str] = mapped_column(String(30))
    ability_id = mapped_column(ForeignKey("csqt_ability.id"))
    ability: Mapped["CSAbility"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))
    language: Mapped["Language"] = relationship(back_populates="ab_langs")

    def get_shortdescription(self):
        if len(self.description) > 150:
            return self.description[0:150]
        else:
            return self.description

class CSFocus(Base):
    """wrapper for a Focus"""
    __tablename__ = "csqt_focus"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cs_page: Mapped[str] = mapped_column(String(30))
    locales: Mapped[List["CSFocusLang"]] = relationship(back_populates="focus")
    abilities_tier1_id = mapped_column(ForeignKey("csqt_focusabilities.id"))
    abilities_tier1: Mapped["CSFocusAbilities"] = relationship(foreign_keys="CSFocus.abilities_tier1_id")
    abilities_tier2_id = mapped_column(ForeignKey("csqt_focusabilities.id"))
    abilities_tier2: Mapped["CSFocusAbilities"] = relationship(foreign_keys="CSFocus.abilities_tier2_id")
    abilities_tier3_id = mapped_column(ForeignKey("csqt_focusabilities.id"))
    abilities_tier3: Mapped["CSFocusAbilities"] = relationship(foreign_keys="CSFocus.abilities_tier3_id")
    abilities_tier4_id = mapped_column(ForeignKey("csqt_focusabilities.id"))
    abilities_tier4: Mapped["CSFocusAbilities"] = relationship(foreign_keys="CSFocus.abilities_tier4_id")
    abilities_tier5_id = mapped_column(ForeignKey("csqt_focusabilities.id"))
    abilities_tier5: Mapped["CSFocusAbilities"] = relationship(foreign_keys="CSFocus.abilities_tier5_id")
    abilities_tier6_id = mapped_column(ForeignKey("csqt_focusabilities.id"))
    abilities_tier6: Mapped["CSFocusAbilities"] = relationship(foreign_keys="CSFocus.abilities_tier6_id")
    charactertemplates: Mapped["CSCharacterTemplate"] = relationship(back_populates="focus")

class CSFocusLang(Base):
    __tablename__ = "csqt_focuslang"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
#    gm_intrusion: Mapped[str] = mapped_column(Text)
    focus_id = mapped_column(ForeignKey("csqt_focus.id"))
    focus: Mapped["CSFocus"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))
    language: Mapped["Language"] = relationship(back_populates="focus_langs")

class CSFocusAbilities(Base):
    __tablename__= "csqt_focusabilities"
    id: Mapped[int] = mapped_column(primary_key=True)
    abilities: Mapped[List[CSAbility]] = relationship(
        secondary=focusabilities_abilities_table,
        back_populates="focusabilities"
        )
    abilities_to_choose: Mapped[List[CSAbility]] = relationship(
        secondary=focusabilities_abilities_to_choose_table,
        back_populates="focusabilities_to_choose"
        )
    # focus_ab_tier1: Mapped["CSFocus"] = relationship(back_populates="abilities_tier1")
    # focus_ab_tier2: Mapped["CSFocus"] = relationship(back_populates="abilities_tier2")
    # focus_ab_tier3: Mapped["CSFocus"] = relationship(back_populates="abilities_tier3")
    # focus_ab_tier4: Mapped["CSFocus"] = relationship(back_populates="abilities_tier4")
    # focus_ab_tier5: Mapped["CSFocus"] = relationship(back_populates="abilities_tier5")
    # focus_ab_tier6: Mapped["CSFocus"] = relationship(back_populates="abilities_tier6")

# association table between tables descriptor and initialink
# https://docs.sqlalchemy.org/en/21/orm/basic_relationships.html#many-to-many
descriptor_initiallink_table = Table(
    "csqt_descriptor_initial_links",
    Base.metadata,
    Column("descriptor_id", ForeignKey("csqt_descriptor.id")),
    Column("initiallink_id", ForeignKey("csqt_initiallink.id")),
)

class CSDescriptor(Base):
    """wrapper for a Focus"""
    __tablename__ = "csqt_descriptor"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cs_page: Mapped[str] = mapped_column(String(30))
    characteristics: Mapped[List["CSDescriptorCharacteristic"]] = relationship(
        secondary=descriptor_characteristics_table,
        back_populates="descriptors"
        )
    initiallinks: Mapped[List["CSInitialLink"]] = relationship(
        secondary=descriptor_initiallink_table,
        back_populates="descriptors"
        )
    characters: Mapped[List["CSCharacter"]] = relationship(
        secondary=character_descriptor_table,
        back_populates="descriptors"
        ) 
    locales: Mapped[List["CSDescriptorLang"]] = relationship(back_populates="descriptor")

class CSDescriptorLang(Base):
    __tablename__ = "csqt_descriptorlang"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    descriptor_id = mapped_column(ForeignKey("csqt_descriptor.id"))
    descriptor: Mapped["CSDescriptor"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))
    language: Mapped["Language"] = relationship(back_populates="descriptor_langs")

class CSDescriptorCharacteristic(Base):
    __tablename__ = "csqt_descriptorcharacteristic"
    id: Mapped[int] = mapped_column(primary_key=True)
    descriptors: Mapped[List["CSDescriptor"]] = relationship(
        secondary=descriptor_characteristics_table,
        back_populates="characteristics"
        )
    name: Mapped[str] = mapped_column(String(50))
    locales: Mapped[List["CSDescriptorCharacteristicLang"]] = relationship(back_populates="descriptorcharacteristic")

class CSDescriptorCharacteristicLang(Base):
    __tablename__ = "csqt_descriptorcharacteristiclang"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    descriptorcharacteristic_id = mapped_column(ForeignKey("csqt_descriptorcharacteristic.id"))
    descriptorcharacteristic: Mapped["CSDescriptorCharacteristic"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))
    language: Mapped["Language"] = relationship(back_populates="descriptorcharacteristic_langs")

class CSInitialLink(Base):
    __tablename__ = "csqt_initiallink"
    id: Mapped[int] = mapped_column(primary_key=True)
    locales: Mapped[List["CSInitialLinkLang"]] = relationship(back_populates="initiallink")
    descriptors: Mapped[List["CSDescriptor"]] = relationship(
        secondary=descriptor_initiallink_table,
        back_populates="initiallinks"
        )
    
class CSInitialLinkLang(Base):
    __tablename__ = "csqt_initiallinklang"
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    initiallink_id = mapped_column(ForeignKey("csqt_initiallink.id"))
    initiallink: Mapped["CSInitialLink"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))


class CSFlavor(Base):
    """wrapper for a Flavor"""
    __tablename__ = "csqt_flavor"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cs_page: Mapped[str] = mapped_column(String(30))
    abilities_rank1: Mapped[List[CSAbility]] = relationship(
        secondary=flavor_abilities_tier1_table,
        back_populates="flavorabilities_rank1"
        ) 
    abilities_rank2: Mapped[List[CSAbility]] = relationship(
        secondary=flavor_abilities_tier2_table,
        back_populates="flavorabilities_rank2"
        )
    abilities_rank3: Mapped[List[CSAbility]] = relationship(
        secondary=flavor_abilities_tier3_table,
        back_populates="flavorabilities_rank3"
        )
    abilities_rank4: Mapped[List[CSAbility]] = relationship(
        secondary=flavor_abilities_tier4_table,
        back_populates="flavorabilities_rank4"
        )
    abilities_rank5: Mapped[List[CSAbility]] = relationship(
        secondary=flavor_abilities_tier5_table,
        back_populates="flavorabilities_rank5"
        )
    abilities_rank6: Mapped[List[CSAbility]] = relationship(
        secondary=flavor_abilities_tier6_table,
        back_populates="flavorabilities_rank6"
        )
    locales: Mapped[List["CSFlavorLang"]] = relationship(back_populates="flavor")
    characters: Mapped[List["CSCharacter"]] = relationship(
        secondary=character_flavor_table,
        back_populates="flavors"
        ) 
    charactertemplates: Mapped["CSCharacterTemplate"] = relationship(back_populates="flavor")

    
class CSFlavorLang(Base):
    __tablename__ = "csqt_flavorlang"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    #gm_intrusion: Mapped[str] = mapped_column(Text)
    flavor_id = mapped_column(ForeignKey("csqt_flavor.id"))
    flavor: Mapped["CSFlavor"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))
    language: Mapped["Language"] = relationship(back_populates="flavor_langs")

class CSCharacterType(Base):
    """wrapper for a Character Type"""
    __tablename__ = "csqt_charactertype"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    might_start: Mapped[int] = mapped_column(Integer)
    speed_start: Mapped[int] = mapped_column(Integer)
    intellect_start: Mapped[int] = mapped_column(Integer)
    might_edge_start: Mapped[int] = mapped_column(Integer)
    speed_edge_start: Mapped[int] = mapped_column(Integer)
    intellect_edge_start: Mapped[int] = mapped_column(Integer)
    cyphers_start: Mapped[int] = mapped_column(Integer)
    cs_page: Mapped[str] = mapped_column(String(30))
    abilities_rank1: Mapped[List[CSAbility]] = relationship(
        secondary=type_abilities_tier1_table,
        back_populates="typeabilities_rank1"
        ) 
    abilities_rank2: Mapped[List[CSAbility]] = relationship(
        secondary=type_abilities_tier2_table,
        back_populates="typeabilities_rank2"
        ) 
    abilities_rank3: Mapped[List[CSAbility]] = relationship(
        secondary=type_abilities_tier3_table,
        back_populates="typeabilities_rank3"
        ) 
    abilities_rank4: Mapped[List[CSAbility]] = relationship(
        secondary=type_abilities_tier4_table,
        back_populates="typeabilities_rank4"
        ) 
    abilities_rank5: Mapped[List[CSAbility]] = relationship(
        secondary=type_abilities_tier5_table,
        back_populates="typeabilities_rank5"
        ) 
    abilities_rank6: Mapped[List[CSAbility]] = relationship(
        secondary=type_abilities_tier6_table,
        back_populates="typeabilities_rank6"
        )
    locales: Mapped["CSCharacterTypeLang"] = relationship(back_populates="charactertype")
    characters: Mapped["CSCharacter"] = relationship(back_populates="charactertype")
    charactertemplates: Mapped["CSCharacterTemplate"] = relationship(back_populates="charactertype")

class CSCharacterTypeLang(Base):
    __tablename__ = "csqt_charactertypelang"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    charactertype_id = mapped_column(ForeignKey("csqt_charactertype.id"))
    charactertype: Mapped["CSCharacterType"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))
    language: Mapped["Language"] = relationship(back_populates="charactertype_langs")


class CSCypher(Base):
    """wrapper for a Cypher"""
    __tablename__ = "csqt_cypher"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cs_page: Mapped[str] = mapped_column(String(50))
    level: Mapped[str] = mapped_column(String(10))
    is_manifeste: Mapped[bool] = mapped_column(Boolean)
    is_fantastic: Mapped[bool] = mapped_column(Boolean)
    is_subtle: Mapped[bool] = mapped_column(Boolean)
    locales: Mapped["CSCypherLang"] = relationship(back_populates="cypher")
    characters: Mapped[List["CSCharacter"]] = relationship(
        secondary=character_cypher_table,
        back_populates="cyphers"
        )


class CSCypherLang(Base):
    __tablename__ = "csqt_cypherlang"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    effect: Mapped[str] = mapped_column(Text)
    hint: Mapped[str] = mapped_column(Text)
    table: Mapped[str] = mapped_column(Text)
    cypher_id = mapped_column(ForeignKey("csqt_cypher.id"))
    cypher: Mapped["CSCypher"] = relationship(back_populates="locales")
    lang_id = mapped_column(ForeignKey("csqt_language.id"))
    language: Mapped["Language"] = relationship(back_populates="cypher_langs")

class CSCharacter(Base):
    """wrapper for a Character"""
    __tablename__ = "csqt_character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    tier: Mapped[int] = mapped_column(Integer)
    might: Mapped[int] = mapped_column(Integer)
    speed: Mapped[int] = mapped_column(Integer)
    intellect: Mapped[int] = mapped_column(Integer)
    might_edge: Mapped[int] = mapped_column(Integer)
    speed_edge: Mapped[int] = mapped_column(Integer)
    intellect_edge: Mapped[int] = mapped_column(Integer)
    charactertype_id = mapped_column(ForeignKey("csqt_charactertype.id"))
    charactertype: Mapped["CSCharacterType"] = relationship(back_populates="characters")
    descriptors: Mapped[List[CSDescriptor]] = relationship(
        secondary=character_descriptor_table,
        back_populates="characters"
        ) 
    flavors: Mapped[List[CSFlavor]] = relationship(
        secondary=character_flavor_table,
        back_populates="characters"
        ) 
    cyphers: Mapped[List[CSCypher]] = relationship(
        secondary=character_cypher_table,
        back_populates="characters"
        )
    abilities: Mapped[List[CSAbility]] = relationship(
        secondary=character_ability_table,
        back_populates="characters"
        )

class CSCharacterTemplate(Base):
    """wrapper for a Character Template"""
    __tablename__ = "csqt_charactertemplate"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    charactertype_id = mapped_column(ForeignKey("csqt_charactertype.id"))
    charactertype: Mapped["CSCharacterType"] = relationship(back_populates="charactertemplates")
    focus_id = mapped_column(ForeignKey("csqt_focus.id"))
    focus: Mapped["CSFocus"] = relationship(back_populates="charactertemplates")
    flavor_id = mapped_column(ForeignKey("csqt_flavor.id"))
    flavor: Mapped["CSFlavor"] = relationship(back_populates="charactertemplates")
