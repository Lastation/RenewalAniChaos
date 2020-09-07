Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
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

d = 75 + i * 75;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
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
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 2, 1 do

radius = 1 / 4 * math.pi;

d = 75 + i * 75;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
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
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

d = 40 + i * 40;
interval = 10 + i * 10;

x = d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = -d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 5 + 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

d = 160;
interval = 40;

x = d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 20, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 20 + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 20 + 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = -d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 20 + 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Danimoth", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 20 + 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

d1 = 60;
d2 = 200;

x1 = d1;
y1 = 0;

x2 = d2;
y2 = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
      CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x1, y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x2, -y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d1 = 40;
d2 = 120;

x1 = d1;
y1 = d1;

x2 = d2;
y2 = d2;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 4 + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
      CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x1, y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x2, -y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d1 = 60;
d2 = 200;

x1 = 0;
y1 = d1;

x2 = 0;
y2 = d2;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 4 + 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
      CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x1, y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x2, -y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

d1 = 40;
d2 = 120;

x1 = -d1;
y1 = d1;

x2 = -d2;
y2 = d2;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i * 4 + 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(2, "Protoss Dark Templar", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(3, "40 + 1n Mojo", "[Skill]Unit_Wait_5", CurrentPlayer);
      CreateUnit(2, "40 + 1n Gantrithor", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x1, y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x1, -y1);
      MoveUnit(1, "Protoss Dark Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x2, y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x2, -y2);
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Templar", "Anywhere", CurrentPlayer);
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}



end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

d = 160;
interval = 40;

d2 = 120;
interval2 = 30;

x = d;
y = 0;

x2 = d2;
y2 = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Hydralisk", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, -interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval2, -interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval2, -interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval2, -interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Hydralisk", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, -interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval2, -interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval2, -interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval2, -interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -d;
y = 0;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Hydralisk", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval, interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval2, interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval2, interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, interval2, interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 0;
y = -d;

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Hydralisk", "[Skill]Unit_Wait_6", CurrentPlayer);
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_5", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval, interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, x2, y2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval2, interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval2, interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      LMove(167, -interval2, interval2);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 1, 1 do

radius = (i + 0) / 8 * math.pi;

d = 100;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
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

d = 130;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
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
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
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

d = 150;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Goliath", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "40 + 1n Gantrithor", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Gantrithor", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

end



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 220, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(1000);
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}