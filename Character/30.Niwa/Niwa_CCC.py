import Function as f;

var x = 0;
var y = 0;

function main(cp)
{
   MoveUnit(All, "40 + 3n Zeratul", cp, "Anywhere", "[Skill]HoldPosition");

   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "Unclean One (Defiler)", 45, 3, 32);

            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 50);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 50);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         if (f.loop[cp] == 1)
         {
            f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         }
         /*
         if (f.loop[cp] < 8)
         {
            if (f.loop[cp] == 0) { x = 32; y = 0; }
            if (f.loop[cp] == 1) { x = 32; y = 32; }
            if (f.loop[cp] == 2) { x = 0; y = 32; }
            if (f.loop[cp] == 3) { x = -32; y = 32; }
            if (f.loop[cp] == 4) { x = -32; y = 0; }
            if (f.loop[cp] == 5) { x = -32; y = -32; }
            if (f.loop[cp] == 6) { x = 0; y = -32; }
            if (f.loop[cp] == 7) { x = 32; y = -32; }

            f.DotShapeWithProperty(cp, 1, "40 + 1n Lurker", x, y, 0);
         }
         */
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "60 + 1n Hydralisk", 100, 100);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 100);
            f.SquareShapeWithProperty(cp, 1, "60 + 1n Archon", 100, 100, 1);

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 0);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n Hydralisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Hydralisk", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "60 + 1n Hydralisk", 100, 0);
            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 100, 0);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 0);
            f.SquareShapeWithProperty(cp, 1, "60 + 1n Archon", 100, 0, 1);

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 100);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n Hydralisk", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Hydralisk", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 19)
         {
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 9, 50);
            f.EdgeShape(cp, 1, "Protoss Dark Templar", 45, 3, 150);
            f.EdgeShape(cp, 1, "Protoss Dark Templar", 45, 5, 200);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("Protoss Dark Templar", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 3n Zeratul", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

         }
         if (f.loop[cp] == 9)
         {
            f.Voice_Routine(cp, 8);
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 32)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Mutalisk", 3, 50);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 50);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, "Anywhere");
         }
         if (f.loop[cp] == 3)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "40 + 1n Mutalisk", 3, 50);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 50);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, "Anywhere");
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 7)
         {
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (Bring(cp, AtLeast, 2, "Protoss Arbiter", "[Skill]UseSkill")
            )
         {
            f.Voice_Routine(cp, 9);
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 230;
            KillUnitAt(2, "Protoss Arbiter", "[Skill]UseSkill", cp);
         }
         else
         {
            KillUnitAt(All, "40 + 3n Zeratul", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Lurker", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", cp);
            KillUnitAt(All, "Unclean One (Defiler)", "Anywhere", cp);

            f.SkillEnd(cp);
         }
      }
   }
}