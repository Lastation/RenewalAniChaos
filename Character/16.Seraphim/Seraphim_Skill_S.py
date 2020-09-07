x = 50;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 100;
y = 100;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 50;
y = 50;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 50;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      LMove(167, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "16.Seraphim");
      MoveLocation("16.Seraphim", " * Sarah Kerrigan", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "16.Seraphim");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(120);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, " * Sarah Kerrigan");
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Sarah Kerrigan", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}