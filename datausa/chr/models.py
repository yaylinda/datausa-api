from datausa.database import db
from datausa.attrs import consts
from datausa.attrs.models import University
from datausa import cache

from datausa.core.models import BaseModel
from datausa.attrs.consts import NATION, STATE, COUNTY, MSA, ALL
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData

metadata = cache.get("chr_metadata")
if not metadata:
    metadata = MetaData(schema='chr', bind=db.engine)
    metadata.reflect()
    cache.set("chr_metadata", metadata)

AutomapBase = automap_base(bind=db.engine, metadata=metadata)


class HealthYg(AutomapBase, db.Model, BaseModel):
    __table_args__ = {"schema": "chr", "extend_existing": True}
    source_title = 'County Health Rankings'
    source_link = 'http://www.countyhealthrankings.org/'
    source_org = 'University of Wisconsin'
    __tablename__ = 'yg'
    median_moe = 1

    year = db.Column(db.Integer, primary_key=True)
    geo = db.Column(db.String(), primary_key=True)

    @classmethod
    def get_supported_levels(cls):
        return {"geo": [ALL, STATE, COUNTY]}

    @classmethod
    def geo_filter(cls, level):
        if level == ALL:
            return True
        level_map = {STATE: "040", COUNTY: "050"}
        level_code = level_map[level]
        return cls.geo.startswith(level_code)

AutomapBase.prepare(db.engine, reflect=False)
