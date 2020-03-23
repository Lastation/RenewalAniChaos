
x = 96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, 169);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, 169);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, 169);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, 40, 169);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, 169);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
	  Wait(0);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}

x = 96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


x = -32;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = -96;
y = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 4000, 77);
      Deaths(CurrentPlayer, Exactly, 100, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, 77, "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : S");
      PreserveTrigger();
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, 40);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, x, y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      LMove(169, -x, -y);
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, 40, 169);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, 40, 169);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      MoveLocation(169, 77, CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, 169);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
	  Wait(1000);
      SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
   },
}

Trigger { -- ===================================================
	players = {Force1, Force2},
	conditions = {
		Never();
	},
	actions = {
		Comment("===================================================");
	},
}

