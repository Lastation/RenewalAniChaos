import Function as f;

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   MoveUnit(All, "60 + 1n High Templar", cp, "Anywhere", "[Skill]HoldPosition");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 0);
            f.SquareShapeWithProperty(cp, 1, "40 + 1n Mojo", 50, 0, 1);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 2)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 100);
            f.SquareShapeWithProperty(cp, 1, "40 + 1n Mojo", 100, 100, 1);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 150, 0);
            f.SquareShapeWithProperty(cp, 1, "40 + 1n Mojo", 150, 0, 1);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 8)
         {
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 0);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 100, 100);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 150, 0);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         if (f.loop[cp] < 12)
         {
            if (f.loop[cp] % 2 == 0)
            {
               f.SquareShape(cp, 1, "40 + 1n Mojo", 150 - 8 * f.loop[cp], 0);
            }
            if (f.loop[cp] % 2 == 1)
            {
               f.SquareShapeWithProperty(cp, 1, "40 + 1n Mojo", 150 - 8 * f.loop[cp], 0, 1);
            }
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150 - 8 * f.loop[cp], 0);
            f.SquareShape(cp, 1, "Rhynadon (Badlands)", 50, 50);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            f.MoveLoc("60 + 1n High Templar", cp, 0, 0);
            RemoveUnitAt(1, "60 + 1n High Templar", "Anywhere", cp);
            f.SkillUnit(cp, 1, "40 + 1n Guardian");
            f.SkillUnit(cp, 1, " Unit. Schnee");
            f.SkillUnitWithProperty(cp, 1, "40 + 1n Lurker", 0);
            f.SkillUnitWithProperty(cp, 1, "40 + 1n Drone", 0);

            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 17)
         {
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 42)
         {
            KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }
         if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         }
         if (f.loop[cp] == 6)
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);

            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 3, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}