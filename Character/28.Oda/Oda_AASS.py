import Function as f;

function NxNSquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, n, distance, x, y);

function main(cp)
{
   f.BanReturn(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 18)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 13)
         {
            f.EdgeShape(cp, 1, "Bengalaas (Jungle)", 45, 3, 50);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);

            f.DotShape(cp, 1, "Target", 0, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         var d = 100;

         if (f.loop[cp] == 0)
         {
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 3, 50, -d, d);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 3, 50, d, -d);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 3, 50, -d, d);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 3, 50, d, -d);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 1)
         {
            f.DotShape(cp, 6, "40 + 1n Goliath", -d, d);
            f.DotShape(cp, 6, "40 + 1n Goliath", d, -d);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 2)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.DotShape(cp, 1, "50 + 1n Battlecruiser", -d, d);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", d, -d);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 6)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         var d = 100;

         if (f.loop[cp] == 0)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 50, d, d);
            f.NxNSquareShapeAt(cp, 1, "40 + 1n Wraith", 2, 50, -d, -d);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 3, 50, d, d);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 3, 50, -d, -d);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 1)
         {
            f.DotShape(cp, 6, "40 + 1n Goliath", d, d);
            f.DotShape(cp, 6, "40 + 1n Goliath", -d, -d);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 2)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.DotShape(cp, 1, "50 + 1n Battlecruiser", d, d);
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", -d, -d);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] < 4)
         {             
            f.LineShape(cp, 1, "Bengalaas (Jungle)", 180 - 45 * f.loop[cp], 7, 75, 0);
            f.LineShape(cp, 1, "Bengalaas (Jungle)", 180 - 45 * f.loop[cp], 7, 75, 50);
            f.LineShape(cp, 1, "Bengalaas (Jungle)", 180 - 45 * f.loop[cp] + 180, 7, 75, 50);

            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
         }
         else if (f.loop[cp] == 4)
         {
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45, 7, 75, 0);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45, 7, 75, 75);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 225, 7, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 7, 75, 0);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 7, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 225, 7, 75, 75);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

         }
         else if (f.loop[cp] == 7)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 7, 75, 0);
            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 7, 75, 75);
            f.LineShape(cp, 1, "40 + 1n Wraith", 315, 7, 75, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 135, 7, 75, 0);
            f.LineShape(cp, 1, "60 + 1n Archon", 135, 7, 75, 75);
            f.LineShape(cp, 1, "60 + 1n Archon", 315, 7, 75, 75);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 10)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }
         else if (f.loop[cp] == 11)
         {
            f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 7, 75, 0);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 135, 7, 75, 75);
            f.LineShape(cp, 1, "Kakaru (Twilight)", 315, 7, 75, 75);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 7, 75, 0);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 7, 75, 75);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 315, 7, 75, 75);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.Voice_Routine(cp, 26);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         f.SkillEnd(cp);
      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}

function NxNSquareShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, n, distance, x, y)
{
   f.NxNSquareShapeAt(cp, count, Unit, n, distance, x, y);
   f.NxNSquareShapeAt(cp, count, Unit, n, distance, -x, -y);
   f.NxNSquareShapeAt(cp, count, Unit, n, distance, -y, x);
   f.NxNSquareShapeAt(cp, count, Unit, n, distance, y, -x);
}

