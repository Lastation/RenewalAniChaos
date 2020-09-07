Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim_Bozo", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Sarah Kerrigan", CurrentPlayer, "Anywhere", Move, "16.Seraphim_Bozo");
   },
}



for i = 0, 3, 1 do

radius = 0 / 4 * math.pi;

d = 50 + i * 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

radius = 1 / 4 * math.pi;

d = 50 + i * 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 50;

for i = 0, 3, 1 do

radius = (2 * i + 1) / 4 * math.pi;

d = 250;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x + interval / 2, y + interval / 2);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, 0);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, 0, -interval);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, 0);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(200);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 1, 1 do

radius = i / 8 * math.pi;

d = 120;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");      
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");      
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 170;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Marine", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

for i = 0, 1, 1 do

radius = (i + 2) / 8 * math.pi;

d = 120;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");      
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");      
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 170;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Firebat", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      Order("40 + 1n Firebat", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end

for i = 0, 1, 1 do

radius = (i + 4) / 8 * math.pi;

d = 120;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 8, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");      
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");      
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d = 170;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 9, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end


radius = 3 / 8 * math.pi;

d = 100;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(1500);
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

radius = 5 / 8 * math.pi;

d = 170;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 13, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(400);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");

   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 14, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Firebat", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}