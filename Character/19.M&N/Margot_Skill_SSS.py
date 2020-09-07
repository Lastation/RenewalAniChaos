
for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 50 + 20 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(400);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(1500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Wraith", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Wraith", "Anywhere");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "19.M&N");
   },
}


for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 50 + 20 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Protoss Observer", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Zerg Defiler", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      LMove(172, x, y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -x, -y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, -y, x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      LMove(172, y, -x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      MoveUnit(1, "Protoss Observer", CurrentPlayer, "[Skill]Unit_Wait_ALL", "19.M&N");
      KillUnitAt(All, "Protoss Observer", "Anywhere", CurrentPlayer);
      MoveLocation("19.M&N", " * Infested Kerrigan", CurrentPlayer, "Anywhere");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "19.M&N");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(400);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Infested Kerrigan");
      Bring(CurrentPlayer, AtLeast, 1, " * Infested Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 110, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      RemoveUnitAt(All, "Zerg Defiler", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}