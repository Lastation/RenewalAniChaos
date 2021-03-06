import Function as f;

function main(cp)
{
   f.HoldPosition(cp);
   f.BanReturn(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {         
            f.DotShape(cp, 1, "Protoss Dark Templar", 100 - 50 * f.loop[cp], 100);
            f.DotShape(cp, 1, "Protoss Dark Templar", -100 + 50 * f.loop[cp], -100);
            f.DotShape(cp, 1, "40 + 1n Zealot", -100, 100 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Zealot", 100, -100 + 50 * f.loop[cp]);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "Target", 50, 0);
            f.SquareShape(cp, 1, "Target", 100, 0);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 0);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.SquareShape(cp, 1, "Target", 50, 50);
            f.SquareShape(cp, 1, "Target", 100, 100);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 7, 150);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 7, 150);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 200, 125);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 125, 200);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 200, 275);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 275, 200);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 200, 125);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 125, 200);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 200, 275);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 275, 200);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 200, 125);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 125, 200);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 200, 275);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 275, 200);
            f.SquareShape(cp, 1, "60 + 1n Siege", 200, 125);
            f.SquareShape(cp, 1, "60 + 1n Siege", 125, 200);
            f.SquareShape(cp, 1, "60 + 1n Siege", 200, 275);
            f.SquareShape(cp, 1, "60 + 1n Siege", 275, 200);
            f.SquareShape(cp, 1, "50 + 1n Tank", 200, 125);
            f.SquareShape(cp, 1, "50 + 1n Tank", 125, 200);
            f.SquareShape(cp, 1, "50 + 1n Tank", 200, 275);
            f.SquareShape(cp, 1, "50 + 1n Tank", 275, 200);

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.EdgeShape(cp, 1, "40 + 1n Firebat", 0, 5, 150);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Firebat", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Firebat", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 560);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 5, 50, 100);
            f.LineShape(cp, 1, "40 + 1n Wraith", 315, 5, 50, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.LineShape(cp, 1, "Kakaru (Twilight)", 45, 5, 50, 100);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 225, 5, 50, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 5, 50, 100);
            f.LineShape(cp, 1, "40 + 1n Wraith", 225, 5, 50, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 5, 50, 100);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 315, 5, 50, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 5, 100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);


            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }

         else if (f.loop[cp] == 7)
         {
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 75, 150, 150);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 75, -150, -150);
            f.NxNSquareShapeAt(cp, 1, "50 + 1n Tank", 2, 75, 150, 150);
            f.NxNSquareShapeAt(cp, 1, "50 + 1n Tank", 2, 75, -150, -150);

            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 150);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 75, 150, 150);
            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 75, -150, -150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 75, -150, 150);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 75, 150, -150);
            f.NxNSquareShapeAt(cp, 1, "50 + 1n Tank", 2, 75, -150, 150);
            f.NxNSquareShapeAt(cp, 1, "50 + 1n Tank", 2, 75, 150, -150);

            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 75, -150, 150);
            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 75, 150, -150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 1040);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Firebat", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
   if (f.delayB[cp] == 0)
   {
      if (f.count[cp] < 2)
      {
         if (f.loopB[cp] == 0)
         {
            f.SquareShape(cp, 1, "Protoss Dark Archon", 75, 75);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 1)
         {
            f.SquareShape(cp, 1, "60 + 1n Archon", 150, 0);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] = 0;
         }

      }
   }

}